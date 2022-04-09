# -*- coding: utf-8 -*-

import gom
k=100
l=10.0
w=20.0
pom=0.5
skok=[]

for i in range(11):
	skok.append(-2.5+i*pom)


for j in range(100):
	if(w>=0):
		temp2="Plane Y +"+str(w)+"0 mm"
	else:
		temp2="Plane Y -"+str(abs(w))+"0 mm"
	nazwa_plaszczyznyY=temp2

	for i in range(20):
		
		for n in range(11):
			nazwa_linii="Line "+str(k)
			if(l>=0):
				if(skok[n]>=0):
					temp="Plane X +"+str(l)+"0 mm +"+str(skok[n])+"0 mm"
				else:
					temp="Plane X +"+str(l)+"0 mm -"+str(abs(skok[n]))+"0 mm"
			else:
				if(skok[n]>=0):
					temp="Plane X -"+str(abs(l))+"0 mm +"+str(skok[n])+"0 mm"
				else:
					temp="Plane X -"+str(abs(l))+"0 mm -"+str(abs(skok[n]))+"0 mm"
			nazwa_plaszczyzny=temp
	
	
			MCAD_ELEMENT=gom.script.primitive.create_line_by_intersection (
				name=nazwa_linii, 
				plane1=gom.app.project.actual_elements[temp], 
				plane2=gom.app.project.actual_elements[temp2], 
				properties=gom.Binary ('eAHFlk1sVGUUhp8KIlQQC4iEGL0pVSswtIWKdShQtSAh/BisQEx0nM7caUc6P525tS2mMuxcaVwY3akR46KGyMq4IOLCxIQEF0aDbsS41MSEjYkmYN5z55u50z/Kwngbwjf3nu8957znd6CQix1/fNsEB/Y91b/vGAOlZDYox+P7Rvycnw+eKxWKfinI+mXCp4mlrGqmmVU0rwIuHexPDgPPHj3sPV/IBOPJku9t7+zq8Q4Ugkx2wnsivHdlejk77D58/mmnvbvWn5iyw/zPemDDZ1emm3gAWAmVNFnKFBkhySQJymQ5jc/U8SvTd7ARuBsq/Q1ShymQxufFzQ5pg5nUxD3AnVApkyPJCCN8+9Kf3fqyHbgfKj4j+ORI2PcsQ+TJ4ZMnIEEJn1HGyNopTXJKVqwElkJlkAIFRnj5vBDlOpXlzgQ5UwdPUSBXA/6kTzD3AsvMuIASWfIM0X5V95eGjFVo0q82kGwELU2JJOMkKNjNIbt98YhQRekKqAyZxm0cxyfFDtKMbhHaI0BrlR7R1Pj09Hkf/NLV9nX/pVfOvf2RZDwQjXNqd8HZuC3qT5oCYwwase8PCGM50HHt4tWf3nqhr/uy3symf5isBTFBlgwJxsgTslZkjMDov9S7KPodBXX6ywxTYJzf3lsYoKnypqzrBcWwASAgyZDZJ+4Vq/Ds4+KXIiBLgTwnzkjNZmBtJBJHGeRVi0bAMXwy+HZffvocsuRVTiiRLJmqT4vFaiuwrsGmMcpmQ8pSNzUjGy5nFuVqO7DmFrAuzIPTi4J0+aoSHkRBSDBIkhSnGKJk2ZEnzRcxwR0BHobKgMU6Tpz9ltHb7XyohvE0SfNXb3WeifaMlaLq4ew34kuOyRLpUP5Vn8rwzDe0459zN0RFo91CVF6WjGmn4/B3wnWJ5mqtbkPXSSGuCWvH4let6Zt7z378qH6rDlsW1JartrUze6VLtdoMladNf2iRa3yrTYOaoyzS2bWovOWjT+L6G1/qfQ9IrsFHeZU3KWWm0BPWCu0e41aXAcOcXiY7XD+Qr423TtQkf/hLuhbXiJ1fUdYzhh1w40NpXAeKYI3l/dWv77wrLQeA/qrXceC+mqSGx6RVZ9jg59IQBiV8zv+x+iGhaHqtn2GRy9titU8nrG6V3+pyaa5/JUsd67MHQ7WxHAQ23RK6zCmyFCkadIJhfJK1JHShKTP6Y1SpppRoOXlBmqrpRp+NkLlIdj3xxmQUZbbp1Znm4h5lMWQ2HNY6X+gQ1PxzzfFzhKTNwsTP8xkntAkCbv69MOKaZXDXEiq9DBOQY4Q96BwSprP0qHd7Vr0iKBzuu2mli1Y8i6Ok9Ga02smFFlrQSofhKI8mLdqenRQc3XByHaQoU6aVPTSzAs/+imzFs2ryeB2PcTTndCdma476mHqaJDULYozbfCmyC4+pGlIvHRELZE9Hg5cKW5pJvIiUrHOVJFzf+qo8i9NNJ52moy5R9zCO+kapujTtMp96jcUw3z0GGYp0Q2naRCbyJ17rePouC13fikXuxtlEis7aP9nUKFvHiVO2DqyOJDnZV6puPzHrXUXidFJkYo7vQg1MSnNmPin5lzGO5pMIN66QRycjfxVJrZiKahotsuoU8r3Tvke90tsw+9wtlw31WzGTCJkvVf9Pz+L1NWNUm0e4B8Qii2ycnHGVtqiJsUbbYvY+9LZ7zu+Nvs6FUGd9rq8zOXe5FHqbn+XNYrOxzfxVbrdb/akHKb/COe3qU0u9Ng1NAmWv6u4x2qx6nAWypsOY/f8ZnjsG/xXDjR1h5213hDbrHWGXCPBor3VS9bxWtlj+6uxGTbjVq//tJmN5qo1u4YgoNmH26+Q6UPhb2aWuF/6qT4Br/2iuPAismjGxwmrRQqvcSe2Mjr7ZA1RbeF9LdEapS2dtm6jvgr8+KZTb3QXXfl++2dPy+5J/AbzXApsBD6s='))
			k=k+1
		l=l-10.0
	w=w-0.5
	l=10.0
