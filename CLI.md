Neterial CLI
============

Command-line interface for [Neterial](https://neterial.io) services.

## Features

- Install a Kubernetes cluster in your Hetzner Cloud account
- Add or remove worker nodes
- Includes out-of-the-box support for Cilium CNI, Metrics Server, Hetzner Cloud Controller Manager, and Hetzner CSI.

## Quick start

Creating a Kubernetes cluster named `default` in your Hetzner Cloud account.

You need to have a Hetzner Cloud account. If you don't have one yet, you can
register with **[our referral link](https://hetzner.cloud/?ref=Ij0zPoexotZb)**
and receive €20 in Hetzner Cloud credits.

1. Login

    ```sh
    docker run --pull=always --rm -ti -p 9999:9999 -v neterial:/app/config \
        ghcr.io/neterialio/cli init
    ```

2. Create a Kubernetes cluster

    ```sh
    docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube create cluster
    ```

3. Get the kubeconfig

    ```sh
    docker run --rm -v neterial:/app/config \
        ghcr.io/neterialio/cli kube get kubeconfig > default-kubeconfig
    ```

4. Work with your cluster

    ```sh
    kubectl --kubeconfig default-kubeconfig get nodes
    ```

## More commands

### Creating a cluster with a custom name

```sh
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube create cluster \
    --name thename
```

### Listing all clusters

```sh
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube get clusters
```

### Creating a cluster with 2 worker nodes in Ashburn, USA

```sh
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube create cluster \
  --name thename --location ash --worker-count 2
```

### Showing help and available flags for the "kube create cluster" command

```sh
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube create cluster -h
```

### Adding a node

```sh
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube create node \
    --cluster thename
```

### Removing a node

```sh
# List all nodes
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube get nodes \
    --cluster thename

# Remove a specific node
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube delete node \
    --cluster thename --node thenodename
```

## Resources configuration (VM, CPU, RAM, DISK)

You can choose the VM used for the worker. This is how you can control the compute capacity of your cluster.

### Adding a node with a specific configuration

```sh
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube create node \
    --cluster thename --vm-type VM_TYPE
```

### Creating a cluster with specific worker nodes

```sh
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube create cluster \
    --name thename --worker-vm-type VM_TYPE
```

See the **[full list of VM types](https://docs.hetzner.com/cloud/servers/overview/#server-types)** for available options.

## Cleaning up the system

1. Remove a cluster or multiple clusters

    ```sh
    docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube delete cluster --name thename
    ```

2. Remove the Docker image

    ```sh
    docker rmi ghcr.io/neterialio/cli
    ```

3. Remove the volume with the config file

    ```sh
    docker volume rm neterial
    ```

### Removing your account

> **⚠️ Warning: This operation will permanently remove your Neterial account.**
> You will still have access to your clusters, but you will no longer be able to manage them using the Neterial platform.

```sh
docker run --rm -ti -v neterial:/app/config ghcr.io/neterialio/cli account delete
```

That's it.

