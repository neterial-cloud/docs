Getting started
===============

This guide will take you from initial registration to a running
Kubernetes cluster using the CLI. You can also do this in the UI `web
console <https://console.neterial.io>`__

Plan
----

1. `Sign up for Neterial <#_1-sign-up-for-neterial>`__
2. `Connect your cloud provider <#_2-connect-your-cloud>`__
3. `Create a Kubernetes cluster <#_3-create-the-cluster>`__
4. `Access your cluster <#_4-get-access-to-the-cluster>`__

1. Sign up for Neterial
-----------------------

Install CLI:

.. code:: sh

   curl -sSL https://get.neterial.io/cli.sh | bash

Sign up and log in with the Neterial CLI:

.. code:: sh

   neterial auth login

2. Connect your cloud
---------------------

Neterial installs and manages resources in your cloud account and
requires access credentials for your chosen provider.

Choose one of the following cloud providers: \* `Connect Hetzner
Cloud <Cloud-providers/connect-hetzner-cloud.md>`__ \* `Connect AWS
cloud <Cloud-providers/connect-aws.md>`__

Each guide will walk you through the necessary permissions and
authentication setup.

Verify that the cloud is connected:

.. code:: sh

   neterial provider list

Example output:

.. code:: console

   NAME            STATUS          LAST_UPDATE
   AWS             Uninitialized
   Hetzner Cloud   Ready           2 seconds

3. Create the cluster
---------------------

Create a Kubernetes cluster with the following command:

.. code:: sh

   neterial kube create cluster --cloud [PROVIDER]

Replace: - ``PROVIDER`` with either ``hcloud`` (for Hetzner Cloud) or
``aws`` (for AWS)

Verify that your cluster was created successfully:

.. code:: sh

   neterial kube get clusters

Example output:

.. code:: console

   NAME      STATUS   PROVIDER        LOCATION   AGE          VERSION
   default   Ready    Hetzner Cloud   hel1       5 minutes    1.32

4. Get access to the cluster
----------------------------

.. code:: sh

   kubectl config use-context default-neterial-admin@default-neterial
   kubectl get nodes

Verify that you can access your cluster:

.. code:: sh

   kubectl get nodes

Example output:

.. code:: console

   NAME                       STATUS   ROLES           AGE     VERSION
   nks-default-ctl-1d39beb8   Ready    control-plane   9m39s   v1.32.3
   nks-default-wrk-5a451893   Ready    <none>          8m35s   v1.32.3

Congratulations! You now have a fully operational Kubernetes cluster
managed by Neterial.

Next step
---------

Now that your cluster is running, you can `Deploy Your First
App <deploy-your-first-app.html>`__.
