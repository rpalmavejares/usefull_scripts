import sys

cluster_file = open(sys.argv[1])
annotation_file= open(sys.argv[2])


annotation_dict=dict()

for lines in annotation_file:

    aux=lines.split("\t")
    annotation_dict[aux[0]]=aux[8]
    #print(aux[0]+"\t"+aux[8])
    
for cluster_lines in cluster_file:

    gene_cluster=cluster_lines.split("\t")
    core_gene=gene_cluster[0]
    sub_gene=gene_cluster[1].rstrip("\n")

    if(core_gene in annotation_dict.keys() and sub_gene in annotation_dict.keys()):
        #print(core_gene+"\t"+annotation_dict[core_gene])
        if(annotation_dict[core_gene] == "-" and  annotation_dict[sub_gene] !="-"):
            print(sub_gene+"\t"+annotation_dict[sub_gene])
        
        if(annotation_dict[core_gene] == "-" and annotation_dict[sub_gene] =="-"):
            print(sub_gene+"\t"+annotation_dict[core_gene])
        
        if(annotation_dict[core_gene] != "-" and annotation_dict[sub_gene] =="-"):
            print(sub_gene+"\t"+annotation_dict[core_gene])
            print("recovered")
        
        if(annotation_dict[core_gene] != "-" and annotation_dict[sub_gene] !="-"):
            
            print(sub_gene+"\t"+annotation_dict[sub_gene])
            if(annotation_dict[core_gene] != annotation_dict[sub_gene] ):
                print("missplaced")
    
    if(core_gene not in annotation_dict.keys() and sub_gene in annotation_dict.keys()):
        print(sub_gene+"\t"+annotation_dict[sub_gene])
        print("recovered")

    if(core_gene not in annotation_dict.keys() and sub_gene not in annotation_dict.keys()):
        print(sub_gene+"\t-")

