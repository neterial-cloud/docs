# Getting started

This guide will take you from initial registration to a running
Kubernetes cluster.

## Plan:
1. [Sign up for Neterial](#_1-sign-up-for-neterial)
2. [Connect your cloud provider](#_2-connect-your-cloud)
3. [Create a Kubernetes cluster](#_3-create-the-cluster)
4. [Access your cluster](#_4-get-access-to-the-cluster)

## 1. Sign up for Neterial

Sign up and log in with the Neterial CLI:

```sh
docker run --pull=always --rm -ti -p 9999:9999 -v neterial:/app/config \
  ghcr.io/neterialio/cli auth login
```

## 2. Connect your cloud

Neterial installs and manages resources in your cloud account and requires
access credentials for your chosen provider.

Choose one of the following cloud providers:
* [Connect Hetzner Cloud](Cloud-providers/connect-hetzner-cloud.md)
* [Connect AWS cloud](Cloud-providers/connect-aws.md)

Each guide will walk you through the necessary permissions
and authentication setup.

Verify that cloud connected:

```sh
docker run --rm -ti -v neterial:/app/config \
  ghcr.io/neterialio/cli provider list
```

Example output:
```console
NAME            STATUS          LAST_UPDATE
AWS             Uninitialized
Hetzner Cloud   Ready           2 seconds
```

## 3. Create the cluster

Create a Kubernetes cluster with the following command:

```sh
docker run --rm -ti -v neterial:/app/config \
  ghcr.io/neterialio/cli kube create cluster --cloud=PROVIDER
```

Replace:
- `PROVIDER` with either `hcloud` (for Hetzner Cloud) or `aws` (for AWS)

Verify that your cluster was created successfully:

```sh
docker run --rm -ti -v neterial:/app/config \
  ghcr.io/neterialio/cli kube get clusters
```

Example output:
```console
NAME      STATUS   PROVIDER        LOCATION   AGE          VERSION
default   Ready    Hetzner Cloud   hel1       5 minutes    1.32
```

## 4. Get access to the cluster

Get kubeconfig

```sh
docker run --rm -v neterial:/app/config \
  ghcr.io/neterialio/cli kube get kubeconfig > default-kubeconfig
export KUBECONFIG='default-kubeconfig'
```

Verify that you can access your cluster:

```sh
kubectl get nodes
```

Example output:
```console
NAME                       STATUS   ROLES           AGE     VERSION
nks-default-ctl-1d39beb8   Ready    control-plane   9m39s   v1.32.3
nks-default-wrk-5a451893   Ready    <none>          8m35s   v1.32.3
```

Congratulations! You now have a fully operational Kubernetes cluster
managed by Neterial.

## Next step

Now that your cluster is running,
you can **[Deploy Your First App](Guides/deploy-your-first-app.md)**.

