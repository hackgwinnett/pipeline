<h3>Adding Data Containers</h3>
<img src="https://github.com/hershyz/pipeline/blob/main/assets/bar.png"/>

<p>First, we want to import the client <code>(client.py Python API wrapper)</code> and set a target server address.</p>
<img src="https://raw.githubusercontent.com/hershyz/pipeline/main/assets/import%20client%20and%20set%20address.png"/>

<p>
  Then, we can begin setting the contents of the data containers created on the server-side.<br>
  Data container args are stored in the form of a 2D array when sent to the client API wrapper.<br>
  <code>arr[n][0] = field, arr[n][1] = value</code>
</p>
<img src="https://raw.githubusercontent.com/hershyz/pipeline/main/assets/adding%20container%20contents.png"/>

<p>Finally, we construct arguments using the client and send them to the server.</p>
<img src="https://raw.githubusercontent.com/hershyz/pipeline/main/assets/send%20add%20args.png"/>
