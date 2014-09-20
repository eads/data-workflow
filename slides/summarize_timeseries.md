## Summarize: Time series by category

<pre><code class="sql" data-trim>
select
  c.name,
  sum(quantity * acquisition_cost) as total_cost,
  extract(year from ship_date) as year

from data as d

join codes as c on d.federal_supply_category = c.code
group by c.name, year
order by year desc
</code></pre>
