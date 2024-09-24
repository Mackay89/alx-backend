import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Handle connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Add key-value pairs to the hash "HolbertonSchools"
client.hset("HolbertonSchools", "Portland", 50, redis.print);
client.hset("HolbertonSchools", "Seattle", 80, redis.print);
client.hset("HolbertonSchools", "New York", 20, redis.print);
client.hset("HolbertonSchools", "Bogota", 20, redis.print);
client.hset("HolbertonSchools", "Cali", 40, redis.print);
client.hset("HolbertonSchools", "Paris", 2, redis.print);

// Retrieve all key-value pairs from the hash "HolbertonSchools"
client.hgetall("HolbertonSchools", (err, reply) => {
  if (err) {
    console.error(`Error retrieving data: ${err}`);
  } else {
    console.log(reply); // Output all the key-value pairs
  }

  // Close the Redis client connection
  client.quit();
});

