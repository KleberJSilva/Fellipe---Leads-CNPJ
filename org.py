import pandas as pd

# Listas com os valores
listas = [

['11481104000181', '21878399000188', '21726669000135', '07017622000171', '28140251000190', '27068205000246', '34593464000170', '37338751000122', '35009719000178', '37153529000155', '38449608000170', '39829401000194', '39778429000140', '46123997000178', '46322081000147', '47070979000138', '47348684000180', '48312559000183', '52038455000108', '51862673000191', '39658535000190', '23353151000129', '11481104000181', '10758591000114', '13195725000124', '24793438000132', '49460038000136', '52325755000160', '52673603000158', '47319324000150', '47928059000108', '50416784000101', '49476350000118', '48560563000160', '48376150000120', '40122591000194', '40907773000170', '41676853000125', '41865530000180', '43499283000170', '40907773000170', '41676853000125', '41865530000180', '43499283000170', '43607568000188', '44411391000102', '44697739000170', '41317521000154', '53909471000183', '54884370000168', '54731507000144', '31228795000113', '26884449000153', '31854355000171', '26716919000170', '24339925001878', '33468276000158', '26965746000123', '36429369000161', '37723696000194', '55987501000103', '57644758000180', '21878399000188', '21726669000135', '10241189000168', '27068205000246', '07017622000171', '47070979000138', '47348684000180', '46123997000178', '46322081000147', '46726312000188', '34593464000170', '40819715000195', '37153529000155', '37338751000122', '39829401000194', '39778429000140', '35009719000178', '38449608000170', '35009719000178', '38449608000170', '51862673000191', '52038455000108', '47602940000114', '28140251000190', '55358690000147', '55370398000140', '53709843000128', '48312559000183', '51753851000146', '54694881000117', '54651730000181', '44615414000109', '44897550000120', '46764980000108', '47435356000111', '47759223000109', '46221573000146', '48364995000104', '29713688000139', '23949664000105', '33259865000126', '35182791000100', '07644533000155', '36224644000100', '22428610000123', '19962959000136', '22902694005316', '23925310000112', '39768003000105', '42043689000181', '43088015000166', '41949752000180', '43526620000171', '46080392000147', '49089197000176', '48591284000164', '46364763000112', '17561613000109', '32905769000145', '33394828000120', '41776301000199', '13195725000205', '19693341000118', '54077132000140', '53793860000196', '49632899000154', '49952894000109', '54806123000143', '53191027000175', '51829007000151', '52215583000171', '20403342000160', '23889735000113', '25143872000130', '29067997000189', '44615414000109', '44897550000120', '42309347000756', '42309347000756', '51458600000139', '51453159000100', '47759223000109', '48364995000104', '48925128000192', '47401787000167', '47435356000111', '46764980000108', '46221573000146', '46410798000140', '56961801000178', '34781619000100', '35848273000175', '31509152000148', '52870941000180', '55868937000175', '55915117000197', '57640388000102', '22428610000123', '17561613000109', '22902694005316', '19962959000136', '07644533000155', '24386009000140', '33259865000126', '35182791000100', '36224644000100', '41949752000180', '42043689000181', '43526620000171', '43088015000166', '27068205000165', '27069354000149', '26349751000101', '23925310000112', '23949664000105', '27389474000123', '29713688000139', '49837663000154', '49886663000144', '49089197000176', '48591284000164', '46364763000112', '46080392000147', '49482973000101', '39768003000105', '53732036000126', '53311580000102', '55825597000103', '52213404000167', '52750647000134', '51861658000129', '53321893000133', '53172587000182', '52423409000114', '55442501000110', '57414079000114', '13329284000106', '26605869000153']

]

# Unindo todas as listas em uma só
tudo_junto = [item for sublist in listas for item in sublist]

# Criando um DataFrame com uma única coluna
df = pd.DataFrame(tudo_junto, columns=['CNPJ'])

# Salvando o resultado em um arquivo Excel
df.to_excel('MAUADIADCARAJUNDITAINDA.xlsx', index=False)

print("Arquivo Excel salvo com sucesso!")
