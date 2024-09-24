#!/usr/bin/env yarn dev
import { createQueue } from 'kue';

const queue = createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber}, with message:`,
    message,
  );
};

// Process jobs in the queue
queue.process('push_notification_code', (job, done) => {
  try {
    sendNotification(job.data.phoneNumber, job.data.message);
    done(); // Mark the job as completed
    console.log(`Job ${job.id} completed successfully`);
  } catch (error) {
    console.error(`Job ${job.id} failed:`, error);
    done(new Error('Notification sending failed')); // Mark the job as failed
  }
});

// Graceful shutdown
process.on('SIGINT', () => {
  console.log('Shutting down gracefully...');
  queue.shutdown(5000, (err) => {
    console.log('Kue queue shutdown complete:', err || 'No errors');
    process.exit(0);
  });
});
