#!/usr/bin/yarn dev
import express from 'express';
import { promisify } from 'util';
import { createClient } from 'redis';

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

const app = express();
const client = createClient();
const PORT = 1245;

/**
 * Modifies the reserved stock for a given item.
 * @param {number} itemId - The id of the item.
 * @param {number} stock - The stock of the item.
 */
const reserveStockById = async (itemId, stock) => {
  await promisify(client.SET).bind(client)(`item.${itemId}`, stock);
};

/**
 * Retrieves the reserved stock for a given item.
 * @param {number} itemId - The id of the item.
 * @returns {Promise<String>}
 */
const getCurrentReservedStockById = async (itemId) => {
  return promisify(client.GET).bind(client)(`item.${itemId}`);
};

const getItemById = (id) => {
  return listProducts.find(obj => obj.itemId === id);
};

app.get('/list_products', (_, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId(\\d+)', async (req, res) => {
  const itemId = Number.parseInt(req.params.itemId);
  const productItem = getItemById(itemId);

  if (!productItem) {
    return res.status(404).json({ status: 'Product not found' });
  }

  try {
    const reservedStock = Number.parseInt(await getCurrentReservedStockById(itemId) || 0);
    productItem.currentQuantity = productItem.initialAvailableQuantity - reservedStock;
    res.json(productItem);
  } catch (error) {
    console.error('Error fetching reserved stock:', error);
    res.status(500).json({ status: 'Internal server error' });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number.parseInt(req.params.itemId);
  const productItem = getItemById(itemId);

  if (!productItem) {
    return res.status(404).json({ status: 'Product not found' });
  }

  try {
    const reservedStock = Number.parseInt(await getCurrentReservedStockById(itemId) || 0);
    if (reservedStock >= productItem.initialAvailableQuantity) {
      return res.status(400).json({ status: 'Not enough stock available', itemId });
    }
    await reserveStockById(itemId, reservedStock + 1);
    res.json({ status: 'Reservation confirmed', itemId });
  } catch (error) {
    console.error('Error reserving stock:', error);
    res.status(500).json({ status: 'Internal server error' });
  }
});

const resetProductsStock = async () => {
  return Promise.all(
    listProducts.map(item => promisify(client.SET).bind(client)(`item.${item.itemId}`, 0))
  );
};

app.listen(PORT, async () => {
  try {
    await resetProductsStock();
    console.log(`API available on localhost port ${PORT}`);
  } catch (error) {
    console.error('Error resetting product stock:', error);
  }
});

export default app;

