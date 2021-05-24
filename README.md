<img src="https://raw.githubusercontent.com/hershyz/pipeline/main/assets/pipeline.png" width="200px">

<br>

<p>
  Send and retrieve data anonymously through a remote Flask server.<br>
</p>
<img src="https://raw.githubusercontent.com/hershyz/pipeline/main/assets/bar.png"/>

<h3>Contents</h3>
<ul>
  <li><a href="https://github.com/hershyz/pipeline/blob/main/server.py">Server Source</a></li>
  <li><a href="https://github.com/hershyz/pipeline/blob/main/client.py">Client (Python API Wrapper)</a></li>
</ul>

<h3>Docs</h3>
<ul>
  <li><a href="https://github.com/hershyz/pipeline/blob/main/docs/adding%20data%20containers.md">Adding Data Containers</a></li>
  <li><a href="https://github.com/hershyz/pipeline/blob/main/docs/reading%20and%20parsing%20existing%20data.md">Reading and Parsing Existing Data</a></li>
  <li><a href="https://github.com/hershyz/pipeline/blob/main/tests/tests.py">Tests File</a></li>
</ul>

<h3>Client Commands</h3>
<table>
<tbody>
  <tr>
    <td>client.create_add_args(2D_arr, password, filename)</td>
    <td>2D array is set in the format: arr[n][0] = field, arr[n][1] = value.<br>A password and filename are also needed to create a new data container.</td>
  </tr>
  <tr>
    <td>client.create_read_args(filename, password)</td>
    <td>Returns raw container data when given a filename and password of an existing data container.</td>
  </tr>
  <tr>
    <td>client.send(address, args)</td>
    <td>Sends arguments to an instance of the server running on the address.</td>
  </tr>
  <tr>
    <td>client.parse(raw, field)</td>
    <td>Returns the value of a field given raw data.</td>
  </tr>
</tbody>
</table>
