import redis from 'redis';

// Create Redis client
const client = redis.createClient();

// Handle successful connection to the Redis server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle error events
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Subscribe to a channel
client.subscribe('holberton school channel');

// Listen for messages on the subscribed channel
client.on('message', (channel, message) => {
  console.log(`Received message: ${message} from channel: ${channel}`);

  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit(); // Close the Redis client connection
  }
});

// Function to publish messages with a delay
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message, (err,

