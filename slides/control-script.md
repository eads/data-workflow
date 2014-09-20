## Control script

<pre><code class="bash" data-trim>
#!/bin/bash

echo 'IMPORT DATA'
echo '-----------'
./import.sh

echo 'CREATE SUMMARY FILES'
echo '--------------------'
./summarize.sh

echo 'EXPORT PROCESSED DATA'
echo '---------------------'
./export.sh
</code></pre>
