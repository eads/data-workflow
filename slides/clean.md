## Clean the data:<br/>Convert Excel data to CSV with Python

* Parse the date field, which represents dates in two different formats
* Strip out extra spaces from any strings (of which there are many)
* Split the National Stock Number into two additional fields:
    * First two digits represent the "federal supply group" (e.g. "WEAPONS").
    * First four digits represent the "federal supply class" (e.g. "Guns, through 30 mm").

<hr/>

<pre><code class="python" data-trim>
# NSN parsing example
if header == 'nsn':
    nsn_parts = cell_value.split('-')
    row_dict['federal_supply_class'] = nsn_parts[0]
</code></pre>
