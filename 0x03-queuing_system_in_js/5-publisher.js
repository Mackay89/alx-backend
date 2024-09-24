import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Event handler for successful connection
client.on('connect', function() {
  console.log('Redis client connected to the server');
});

// Event handler for connection errors
client.on('error', function(err) {
  console.log('Redis client not connected to the server: ' + err);
});

// Subscribe to the Redis channel
client.subscribe('holberton school channel');

// Event handler for receiving messages on the channel
client.on('message', function(channel, message) {
  console.log('Message received on channel ' + channel + ': ' + message);

  if (message === 'KILL_SERVER') {
    console.log('Received KILL_SERVER message. Unsubscribing and shutting down the client...');
    client.unsubscribe('holberton school channel'); // Unsubscribe from the specific channel
    client.quit(); // Gracefully quit the Redis client
  }
});
