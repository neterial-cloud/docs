Neterial CLI
============

Command-line interface for [Neterial](https://neterial.io) services.

## Features

- Install a Kubernetes cluster in your Hetzner Cloud account
- Adding/removing worker nodes
- Out-of-the-box: Cilium CNI, Metrics Server, Hetzner Cloud Controller Manager, Hetzner CSI

## Quick start

Creating a Kubernets cluster named `default` in your Hetzner Cloud account.

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

Creating cluster with a name

```sh
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube create cluster \
    --name thename
```

List all clusters

```sh
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube get clusters
```

Create cluster with 2 worker nodes and located in Ashburn USA

```sh
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube create cluster \
  --name thename --location ash --worker-count 2
```

Show help and all flags for "kube create cluster" command

```sh
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube create cluster -h
```

Add a node

```sh
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube create node \
    --cluster thename
```

Remove a node

```sh
# List all nodes
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube get nodes \
    --cluster thename

# Remove the one
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube delete node \
    --cluster hello --node thenodename
```

## Resources configuration (VM, CPU, RAM, DISK)

You can choose the VM used for the worker. This is how you can control the compute capacity of your cluster.

Adding a node with a specific configuration

```sh
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube create node \
    --cluster thename --vm-type VM_TYPE
```

Creating cluster with a specific worker nodes

```sh
docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube create cluster \
    --name thename --worker-vm-type VM_TYPE
```

See
**[the full list of VM-types](https://docs.hetzner.com/cloud/servers/overview/#server-types)**

## Clean up the system

1. Remove the cluster/clusters

    ```sh
    docker run --rm -v neterial:/app/config ghcr.io/neterialio/cli kube delete cluster --name thename
    ```

2. Remove the docker image

    ```sh
    docker rmi ghcr.io/neterialio/cli
    ```

3. Remove the volume with config file

    ```sh
    docker volume rm neterial
    ```

### Removing account

> **Warning**  
> This operation will remove your account completely.
>You will retain access to your clusters, but managing them using the Neterial platform will be unavailable.

```sh
docker run --rm -ti -v neterial:/app/config ghcr.io/neterialio/cli account delete
```

That's it.

