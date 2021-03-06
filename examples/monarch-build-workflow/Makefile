NEO4J_CONTAINER_NAME=ncats-monarch-graph-2019-02-20

run:
	make install
	make download
	python scripts/transform_semmeddb.py
	python scripts/main.py -f

install:
	pip install -r requirements.txt

download:
	# Download data files
	wget --no-clobber http://purl.obolibrary.org/obo/ro.owl -O data/ro.owl || true
	wget --no-clobber https://data.monarchinitiative.org/ttl/clinvar.ttl -O data/clinvar.ttl || true
	wget --no-clobber https://data.monarchinitiative.org/ttl/orphanet.ttl -O data/orphanet.ttl || true
	wget --no-clobber https://data.monarchinitiative.org/ttl/omim.ttl -O data/omim.ttl || true
	wget --no-clobber https://archive.monarchinitiative.org/latest/ttl/hpoa.ttl -O data/hpoa.ttl || true
	wget --no-clobber https://data.monarchinitiative.org/ttl/hgnc.ttl -O data/hgnc.ttl || true
	wget --no-clobber http://34.229.55.225/nodes_neo4j.csv -O data/semmeddb_nodes.csv || true
	wget --no-clobber http://34.229.55.225/edges_neo4j.csv -O data/semmeddb_edges.csv || true
	# Download ontology files
	wget --no-clobber http://purl.obolibrary.org/obo/mondo.owl -O data/mondo.owl || true
	wget --no-clobber https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.owl -O data/hp.owl || true
	wget --no-clobber https://raw.githubusercontent.com/The-Sequence-Ontology/SO-Ontologies/master/so.owl -O data/so.owl || true
	wget --no-clobber http://purl.obolibrary.org/obo/go.owl -O data/go.owl || true
	wget --no-clobber http://purl.obolibrary.org/obo/geno.owl -O data/geno.owl || true

neo4j-start:
	wget --no-clobber https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/3.0.8.6/apoc-3.0.8.6-all.jar --directory-prefix=neo4j/plugins || true
	echo `pwd`
	docker run \
		-d \
		--rm \
		--env NEO4J_dbms_memory_heap_maxSize=5120 \
		--env NEO4J_AUTH=none \
		--name ${NEO4J_CONTAINER_NAME} \
		-p 7474:7474 \
		-p 7473:7473 \
		-p 7472:7687 \
		-v `pwd`/neo4j/plugins:/plugins \
		-v `pwd`/neo4j/data:/data \
		-v `pwd`/neo4j/import:/var/lib/neo4j/import \
		neo4j:3.0

neo4j-stop:
	docker stop ${NEO4J_CONTAINER_NAME}

neo4j-ssh:
	docker exec -it ${NEO4J_CONTAINER_NAME} /bin/bash

neo4j-logs:
	docker logs ${NEO4J_CONTAINER_NAME}

unpack-semmeddb:
	tar -xvf data/transformed_semmeddb.csv.tar -C data/
	sudo mv data/edges.csv data/semmeddb_edges.csv
	sudo mv data/nodes.csv data/semmeddb_nodes.csv

move-results:
	tar -xvf results/clique_merged.csv.tar -C results/
	mv results/edges.csv results/clique_merged_edges.csv
	mv results/nodes.csv results/clique_merged_nodes.csv
	mv results/clique_merged_nodes.csv neo4j/import/
	mv results/clique_merged_edges.csv neo4j/import/
