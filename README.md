# bank-app API

# Parameters to Bank details
#### using IFSC code (GET)
<pre>http://127.0.0.1:8000/search/VALID_IFSC_CODE/</pre>
* * *

<div>

<div>

<div>

#### using city and name of the bank
<pre>http://127.0.0.1:8000/search?bank_name=BANK&city=CITY</pre>

<table class="table table-bordered table-striped table-hover">

<thead>

<tr>

<th>Parameter</th>

<th>Description</th>

</tr>

</thead>

<tbody>

<tr>

<td>bank_name</td>

<td>Name of the bank to search for.</td>

</tr>

<tr>

<td>city</td>

<td>city to search in.</td>

</tr>

</tbody>

</table>
