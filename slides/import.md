## Import data to PostgreSQL

* Import the cleaned CSVs generated from the source data
* Import a "FIPS crosswalk" CSV: Maps county name and state to the Federal Information Processing Standard identifier to identify counties.
* Import a CSV file with Federal Supply Codes
* Import 5 year county population estimates from the US Census Bureau's American Community Survey

<hr/>

<pre><code class="bash" data-trim>
# Example import statement
echo "Import FIPS crosswalk"
psql leso -c "CREATE TABLE fips (
  county varchar,
  state varchar,
  fips varchar
);"
psql leso -c "COPY fips FROM '`pwd`/src/fips_crosswalk.csv' DELIMITER ',' CSV HEADER;"
</code></pre>
