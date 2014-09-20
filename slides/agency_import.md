## Agency import: csvkit magic

* Use csvkit's `in2csv` command to extract each sheet
* Use csvkit's `csvstack` command to combine the sheets and add a grouping column
* Use csvkit's `csvcut` command to remove a pointless "row number" column
* Import final output into Postgres database

<hr/>

<pre><code class="bash" data-trim>
echo "Import agency.csv"
in2csv --sheet "State Agencies" data.xlsx > state_agencies.csv
in2csv --sheet "Federal Agencies" data.xlsx > federal_agencies.csv
in2csv --sheet "Tribal Agencies" data.xlsx > tribal_agencies.csv

csvstack -n "agency_type" -g "state,federal,tribal"
  state_agencies.csv
  federal_agencies.csv
  tribal_agencies.csv | csvcut -c "1,3,4" > agencies.csv
</code></pre>
