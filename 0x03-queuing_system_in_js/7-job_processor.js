#!/usr/bin/env yarn dev
import { createQueue, Job } from 'kue';

const BLACKLISTED_NUMBERS = ['4153518780', '4153518781'];
const queue = createQueue();

/**
 * Sends a push notification to a user.
 * @param {String} phoneNumber - The phone number to send the notification to.
 * @param {String} message - The message to send.
 * @param {Job} job - The Kue job object.
 * @param {Function} done - The callback to signal completion or error.
 */
const sendNotification = (phoneNumber, message, job, done) => {
  let total = 2;
  let pending = 2;

  const sendInterval = setInterval(() => {
    // Update progress
    if (total - pending <= total / 2) {
      job.progress(total - pending, total);
    }

    // Check if the phone number is blacklisted
    if (BLACKLISTED_NUMBERS.includes(phoneNumber)) {
      clearInterval(sendInterval);
      return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    // Simulate sending the notification
    if (total === pending) {
      console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    }

    // Decrease pending count and check if done
    if (--pending === 0) {
      clearInterval(sendInterval);
      done();
    }
  }, 1000);
};

// Process jobs in the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

