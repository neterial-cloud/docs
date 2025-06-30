Ingress-nginx installation
==========================

Official documentation:
https://kubernetes.github.io/ingress-nginx/deploy/

Step 1: Add the Ingress-NGINX Helm repository (if not already added)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

   helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
   helm repo update

Step 2: Create a namespace (optional but recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

   kubectl create namespace ingress-nginx

Step 3: Install Ingress-NGINX with Helm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example with LoadBalancer (Hetzner Cloud).

Create a file named values.yaml:

.. code:: yaml

   controller:
     service:
       type: LoadBalancer
       externalTrafficPolicy: Local
       annotations:
         load-balancer.hetzner.cloud/location: hel1

Add to annotations following field: \*
``load-balancer.hetzner.cloud/location`` - Hetzner network zone for LB
placement

Finally, install ingress-nginx:

.. code:: bash

   helm install ingress-nginx ingress-nginx/ingress-nginx \
     --namespace ingress-nginx \
     -f values.yaml

Load balancer will be created automalically:

.. figure:: _static/img/hetzner-lb.png
   :alt: security

   security

Step 4: Verify installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if the pods are running correctly:

.. code:: bash

   kubectl get pods --namespace ingress-nginx

Check the service status:

.. code:: bash

   kubectl get svc --namespace ingress-nginx

Wait for ``EXTERNAL-IP`` if you're using a cloud-based load balancer.

Step 5: Use Ingress Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After installation, you can create Ingress resources in your
applications:

Example Ingress resource:

.. code:: yaml

   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     name: example-ingress
     namespace: your-app-namespace
   spec:
     ingressClassName: nginx
     rules:
     - host: example.com
       http:
         paths:
         - path: /
           pathType: Prefix
           backend:
             service:
               name: your-service
               port:
                 number: 80

Apply it with:

.. code:: bash

   kubectl apply -f example-ingress.yaml
