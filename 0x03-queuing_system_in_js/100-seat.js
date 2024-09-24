#!/usr/bin/yarn dev
import express from 'express';
import { promisify } from 'util';
import { createQueue } from 'kue';
import { createClient } from 'redis';

const app = express();
const client = createClient({ name: 'reserve_seat' });
const queue = createQueue();
const INITIAL_SEATS_COUNT = 50;
let reservationEnabled = false;
const PORT = 1245;

/**
 * Modifies the number of available seats.
 * @param {number} number - The new number of seats.
 */
const reserveSeat = async (number) => {
  await promisify(client.SET).bind(client)('available_seats', number);
};

/**
 * Retrieves the number of available seats.
 * @returns {Promise<number>}
 */
const getCurrentAvailableSeats = async () => {
  const result = await promisify(client.GET).bind(client)('available_seats');
  return Number.parseInt(result || 0);
};

app.get('/available_seats', async (_, res) => {
  try {
    const numberOfAvailableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats });
  } catch (error) {
    console.error('Error fetching available seats:', error);
    res.status(500).json({ status: 'Internal server error' });
  }
});

app.get('/reserve_seat', async (_req, res) => {
  if (!reservationEnabled) {
    return res.status(403).json({ status: 'Reservations are blocked' });
  }
  
  try {
    const job = queue.create('reserve_seat');
    
    job.on('failed', (err) => {
      console.log('Seat reservation job', job.id, 'failed:', err.message || err.toString());
    });
    
    job.on('complete', () => {
      console.log('Seat reservation job', job.id, 'completed');
    });
    
    job.save();
    res.json({ status: 'Reservation in process' });
  } catch (error) {
    console.error('Error creating reservation job:', error);
    res.status(500).json({ status: 'Reservation failed' });
  }
});

app.get('/process', async (_req, res) => {
  res.json({ status: 'Queue processing' });
  
  queue.process('reserve_seat', async (_job, done) => {
    try {
      const availableSeats = await getCurrentAvailableSeats();
      reservationEnabled = availableSeats > 1 ? true : false;

      if (availableSeats >= 1) {
        await reserveSeat(availableSeats - 1);
        done();
      } else {
        done(new Error('Not enough seats available'));
      }
    } catch (error) {
      console.error('Error processing reservation:', error);
      done(new Error('Error processing reservation'));
    }
  });
});

const resetAvailableSeats = async (initialSeatsCount) => {
  await promisify(client.SET).bind(client)('available_seats', Number.parseInt(initialSeatsCount));
};

app.listen(PORT, async () => {
  try {
    await resetAvailableSeats(process.env.INITIAL_SEATS_COUNT || INITIAL_SEATS_COUNT);
    reservationEnabled = true;
    console.log(`API available on localhost port ${PORT}`);
  } catch (error) {
    console.error('Error initializing available seats:', error);
  }
});

export default app;

