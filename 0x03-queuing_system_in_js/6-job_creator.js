#!/usr/bin/env yarn dev
import { createQueue } from 'kue';

// Create a Kue queue
const queue = createQueue({ name: 'push_notification_code' });

// Create a new job in the queue
const job = queue.create('push_notification_code', {
  phoneNumber: '07045679939',
  message: 'Account registered',
});

// Event listeners for the job
job
  .on('enqueue', () => {
    console.log('Notification job created:', job.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', (error) => {
    console.log('Notification job failed:', error);
  })
  .on('failed', (error) => {
    console.log('Notification job permanently failed:', error);
  });

// Save the job to the queue
job.save((err) => {
  if (err) {
    console.error('Error saving job:', err);
  } else {
    console.log('Job saved successfully');
  }
});

