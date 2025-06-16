# Neterial CLI

Command-line interface for [Neterial](https://neterial.io) services.

## Installation

Linux, macOS (brew), and Windows WSL:

```sh
curl -sSL https://get.neterial.io/cli.sh | bash
```

Read [INSTALL.md](https://github.com/neterialio/cli/blob/main/INSTALL.md) for details and alternative ways to install.

## Quick start

Run to login/signup and discover clouds:

```sh
neterial init
```

## Connect your cloud account

Check your connected clouds:

```sh
neterial provider list
```

### Connect Hetzner Cloud

You need to have a Hetzner Cloud account. If you don't have one yet, you can
register with **[our referral link](https://hetzner.cloud/?ref=Ij0zPoexotZb)**
and receive €20 in Hetzner Cloud credits.

Read [how to create API token in Hetzner Cloud](Cloud-providers/connect-hetzner-cloud.md)

Connect your cloud by adding a Hetzner Cloud API token:

```sh
neterial provider init hcloud
```

### Connect AWS

Read [how to add AWS credentials](Cloud-providers/connect-aws.md)

Connect your cloud by adding AWS credentials:

```sh
neterial provider init aws
```

## Creating Kubernetes cluster

### Creating with the name `default` in `hcloud` cloud

```sh
neterial kube create cluster
```

Get access to the cluster:

```sh
kubectl config use-context default-neterial-admin@default-neterial
kubectl get nodes
```

If you see the nodes, your cluster is ready for work.

### Explicitly set the name and cloud provider

The `--cloud` parameter accepts either `hcloud` or `aws`.

```sh
neterial kube create cluster --name [CLUSTER_NAME] --cloud [CLOUD]
```

### Explicitly set the worker VM type and number of workers

```sh
neterial kube create cluster --worker-vm-type [VM_TYPE] --worker-count [COUNT]
```

### Explicitly set the location

```sh
neterial kube create cluster --cloud [CLOUD] --location [LOCATION]
```

AWS:

```sh
neterial kube create cluster --cloud aws --location us-east-1
```

Hetzner Cloud:

```sh
neterial kube create cluster --cloud hcloud --location ash
```

## Resources configuration (VM, CPU, RAM, DISK)

You can choose the VM used for the worker. This is how you can control the compute capacity of your cluster.

### Adding a worker node with a specific configuration

```sh
neterial kube create node --cluster [CLUSTER_NAME] --vm-type [VM_TYPE]
```

### Creating a cluster with specific worker nodes

```sh
neterial kube create cluster --name thename --worker-vm-type [VM_TYPE]
```

## Adding nodes to the existing cluster

```sh
neterial kube create node --cluster [CLUSTER_NAME]
```

## Removing nodes from the existing cluster

List all nodes:

```sh
neterial kube get nodes --cluster [CLUSTER_NAME]
```

Remove a specific node:

```sh
neterial kube delete node --cluster [CLUSTER_NAME] --node [NODE_NAME]
```

## Removing your account

> **⚠️ Warning: This operation will permanently remove your Neterial account.**
> You will still have access to your clusters, but you will no longer be able to manage them using the Neterial platform.

```sh
neterial account delete
```

