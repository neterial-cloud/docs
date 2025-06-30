# Deploy Your First Application

In this guide, we will deploy a simple test application.
This will help verify that your Kubernetes cluster is running correctly and ready for deployments.
The application is an Nginx web server that serves a single static page.
While simple, this example shows the idea.

## Step 1: Check That Your Cluster is Ready

Run:

```sh
kubectl get nodes
```

You should see a list of nodes like this (node names may vary).

```console
NAME                       STATUS   ROLES           AGE     VERSION
nks-default-ctl-1d39beb8   Ready    control-plane   9m39s   v1.32.3
nks-default-wrk-5a451893   Ready    <none>          8m35s   v1.32.3
```

If so, move to the next step.

## Step 2: Deploy the Application

Create a file named web-app.yaml with the following content, or
[download it here](/Guides/web-app.yaml ':ignore').

[web-app.yaml](web-app.yaml ':include')

Time to deploy. Run:

```sh
kubectl apply -f web-app.yaml
```

You should see:

```console
deployment.apps/web-app created
service/web-app created
```

## Step 3: Check That the Application is Running

### Check if the deployment is ready

Run:

```sh
kubectl get deployment web-app
```

You should see output similar to this:

```console
NAME      READY   UP-TO-DATE   AVAILABLE   AGE
web-app   1/1     1            1           27s
```

### Check if the service is running

Run:

```sh
kubectl get service web-app
```

You should see details of the service.

### Check if the app is available from the Internet

To get the URL for your application, run:

```sh
kubectl get service web-app -o go-template --template=\
'{{range .status.loadBalancer.ingress}}'\
'{{range $key, $val := . }}'\
'{{if eq $key "ip" "hostname"}}http://{{$val}}{{"\n"}}{{end}}'\
'{{end}}'\
'{{end}}'
```

You should see one or more HTTP (http://...) links.

Open the link in a browser. You should see a web page displaying:

>welcome to my web app!

**Note:** It can take several minutes for the application to become available.

If you see the webpage, that means everything is working correctly
and the application has been deployed successfully.

## Clean up

To remove the deployed resources, run:

```sh
kubectl delete -f web-app.yaml
```

You should see:

```console
deployment.apps "web-app" deleted
service "web-app" deleted
```

**Note:** This may take a few minutes.

## Next Steps

This is just a demo. For a production-ready deployment, you should use HTTPS.

One way to achieve this is by using an Ingress controller with Cert-Manager.
You can follow these guides to install them:

* [Install Ingress NGINX](/Guides/ingress-nginx.md)
* [Install cert-manager](/Guides/cert-manager.md)

