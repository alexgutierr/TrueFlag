#!/bin/bash
echo "Restoring database from backup..."
pg_restore --verbose --no-owner --no-acl -U etl_user -d analytics /docker-entrypoint-initdb.d/analytics_backup.dump
echo "Database restoration complete!"