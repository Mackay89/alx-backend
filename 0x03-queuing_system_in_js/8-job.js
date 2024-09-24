#!/usr/bin/env yarn dev
import { Queue, Job } from 'kue';

/**
 * Creates push notification jobs from the array of jobs info.
 * @param {Object[]} jobs - Array of job info objects.
 * @param {Queue} queue - Kue queue instance.
 * @throws Will throw an error if jobs is not an array or if job info is invalid.
 */
export const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  for (const jobInfo of jobs) {
    // Validate jobInfo properties
    if (!jobInfo.phoneNumber || !jobInfo.message) {
      throw new Error('Job info must contain phoneNumber and message');
    }

    const job = queue.create('push_notification_code_3', jobInfo);

    job
      .on('enqueue', () => {
        console.log('Notification job created:', job.id);
      })
      .on('complete', () => {
        console.log('Notification job', job.id, 'completed');
      })
      .on('failed', (err) => {
        console.log('Notification job', job.id, 'failed:', err.message || err.toString());
      })
      .on('progress', (progress, _data) => {
        console.log('Notification job', job.id, `${progress}% complete`);
      });

    job.save((err) => {
      if (err) {
        console.error('Failed to save job:', err.message);
      }
    });
  }
};

export default createPushNotificationsJobs;

