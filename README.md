# conch
A minimal cloud service to facilitate connecting devices over TCP/UDP.

## Overview
JSON is worth a thousand words.
```
my-project: {
  my-device: {
    address: "127.0.0.1",
    port: 4000,
    timestamp: 2019-01-18 17:09:40.734572
  }
  some-other-device {
    address: "127.0.0.3",
    port: 80,
    timestamp: 2019-01-18 17:08:59.612893
  }
}
```

As you can see, devices are organized under projects, the primary organizational grouping within the `conch` service. Every device detailed under a project lists its IP address, the port it's listening on, and an automatic timestamp indicating how recently the device's properties were updated.

## API/Examples
### A simple read-only request
`https://us-central1-landline.cloudfunctions.net/sync?project=my-project`

This call will return the current state of `my-project`.

### A read/write request
`https://us-central1-landline.cloudfunctions.net/sync?project=my-project&device=my-device&address=127.0.0.1&port=4000`

Just like the read-only request, this call will return the current state of `my-project`, *after* adding/updating the `address` and `port` fields under `my-device`. The `timestamp` field is filled automatically any time a read-write request is made.
