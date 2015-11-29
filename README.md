# Apriori-ADB
######Apriori Algorithm
check readme.pdf

Enter File Name (Integrated-Dataset.csv by default) : Integrated-Dataset.csv <br />
Enter Minimum Support (0.05 by default) : 0.05 <br />
Enter Minimum Confidence (0.5 by default) : 0.5 <br />

Table deleted successfully if it ever existed..

Table created successfully

Loaded data in Table from CSV file

Legend Created

Initialization Complete...

Total number of entries in Dataset: 852433.0

---------------Generating Large Itemsets--------------------<br />
Generated 14 1-sized frequent itemsets <br />
Generated 15 2-sized frequent itemsets <br />
Generated 2 3-sized frequent itemsets <br />

Generated a total of 31 frequent itemsets...

---------------Generating Association Rules-----------------<br />
Generated 17 association rules

Apriori Algorithm Completed!!

Table deleted successfully if it ever existed..

Result stored in output.txt

---------------Contents of output.txt-----------------------<br />
Frequent Itemsets (Minimum Support: 0.05)

[type: emergency]: Support ->  61.23273031428863%<br />
[type: non emergency]: Support ->  35.02245924313113%<br />
[category: heat/hot water]: Support ->  31.899633167650716%<br />
[type: emergency, category: heat/hot water]: Support ->  31.709119661017347%<br />
[space: entire apartment]: Support ->  26.812195210649985%<br />
[space: building-wide]: Support ->  18.127055146856115%<br />
[type: emergency, space: entire apartment]: Support ->  17.055885917133665%<br />
[type: emergency, space: building-wide]: Support ->  16.992185896134945%<br />
[category: heat/hot water, space: building-wide]: Support ->  16.475429740519196%<br />
[type: emergency, category: heat/hot water, space: building-wide]: Support ->  16.432493814763156%<br />
[space: bathroom]: Support ->  15.298445742949887%<br />
[category: unsanitary condition]: Support ->  14.113367267574109%<br />
[category: paint/plaster]: Support ->  12.19556258380424%<br />
[space: kitchen]: Support ->  10.625116578077105%<br />
[category: heat/hot water, space: entire apartment]: Support ->  10.582180652321062%<br />
[type: emergency, category: heat/hot water, space: entire apartment]: Support ->  10.435541561624198%<br />
[category: plumbing]: Support ->  9.499514917887975%<br />
[type: non emergency, space: entire apartment]: Support ->  9.054787883622526%<br />
[type: non emergency, category: paint/plaster]: Support ->  8.325346390860044%<br />
[type: emergency, space: bathroom]: Support ->  7.9085394394632775%<br />
[type: non emergency, category: unsanitary condition]: Support ->  7.76671011094127%<br />
[space: bedroom]: Support ->  7.635438796949439%<br />
[category: unsanitary condition, space: entire apartment]: Support ->  6.979316849535389%<br />
[category: door/window]: Support ->  6.908108907092991%<br />
[space: kitchen, type: non emergency]: Support ->  6.562744520683737%<br />
[type: non emergency, space: bathroom]: Support ->  6.468308946274956%<br />
[type: emergency, category: unsanitary condition]: Support ->  6.346657156632839%<br />
[category: water leak]: Support ->  6.064758168677186%<br />
[type: emergency, category: plumbing]: Support ->  5.821337278120392%<br />
[category: plumbing, space: bathroom]: Support ->  5.183867823042984%<br />
[category: electric]: Support ->  5.093420831901159%<br />

Association Rules (Minimum Confidence: 0.5)

[category: heat/hot water, space: building-wide] => [type: emergency]: Confidence - 99.73939419831675%<br />
[category: heat/hot water] => [type: emergency]: Confidence - 99.40277210828066%<br />
[category: heat/hot water, space: entire apartment] => [type: emergency]: Confidence - 98.61428286366761%<br />
[type: emergency, space: building-wide] => [category: heat/hot water]: Confidence - 96.70617962401707%<br />
[space: building-wide] => [type: emergency]: Confidence - 93.73936228732664%<br />
[space: building-wide] => [category: heat/hot water]: Confidence - 90.88861708117342%<br />
[category: paint/plaster] => [type: non emergency]: Confidence - 68.26537384930597%<br />
[space: entire apartment] => [type: emergency]: Confidence - 63.61241883827159%<br />
[space: kitchen] => [type: non emergency]: Confidence - 61.7663295499713%<br />
[category: plumbing] => [type: emergency]: Confidence - 61.28036356002322%<br />
[type: emergency, space: entire apartment] => [category: heat/hot water]: Confidence - 61.18440057775637%<br />
[category: unsanitary condition] => [type: non emergency]: Confidence - 55.030879333704604%<br />
[category: plumbing] => [space: bathroom]: Confidence - 54.56981612062685%<br />
[type: emergency, category: heat/hot water] => [space: building-wide]: Confidence - 51.82261125642344%<br />
[type: emergency] => [category: heat/hot water]: Confidence - 51.78459215890629%<br />
[space: bathroom] => [type: emergency]: Confidence - 51.69505172189035%<br />
[category: heat/hot water] => [space: building-wide]: Confidence - 51.647709094118554%<br />
