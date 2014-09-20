## Summarize: Total cost by category

<pre><code class="sql" data-trim>
select
  c.full_name,
  c.code as federal_supply_class,
  sum((d.quantity * d.acquisition_cost)) as total_cost

from data as d

join codes as c on d.federal_supply_class = c.code

group by c.full_name, c.code

order by c.full_name
</code></pre>
