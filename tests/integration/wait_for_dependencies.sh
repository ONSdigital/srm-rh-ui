#!/usr/bin/env bash
RH_SVC_CONTAINER=rh-service-rh-ui-it
echo "Waiting for [$RH_SVC_CONTAINER] to be ready"

while true; do
  response=$(docker inspect $RH_SVC_CONTAINER -f "{{ .State.Health.Status }}")
  if [[ "$response" == "healthy" ]]; then
    echo "[$RH_SVC_CONTAINER] is ready"
    break
  fi

  echo "[$RH_SVC_CONTAINER] not ready ([$response] is its current state)"
  ((attempt++))
  if [[ attempt -eq 30 ]]; then
    echo "[$RH_SVC_CONTAINER] failed to start"
    exit 1
  fi
  sleep 2

done

echo "Containers running and alive"
