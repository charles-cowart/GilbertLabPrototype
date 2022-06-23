from sequence_processing_pipeline.QCJob import QCJob

fastq_root_dir = "/Users/ccowart/Development/ForCarolina/mg-scripts/fastq_root_dir"
output_path = "/Users/ccowart/Development/ForCarolina/mg-scripts/output_path"
modules_to_load = None
fastp_path = "/Users/ccowart/Development/ForCarolina/mg-scripts/bin/fake_fastp"
minimap2_path = "/Users/ccowart/Development/ForCarolina/mg-scripts/bin/fake_minimap2"
samtools_path = "/Users/ccowart/Development/ForCarolina/mg-scripts/bin/fake_samtools"
sample_sheet_path = "/Users/ccowart/Development/ForCarolina/mg-scripts/sequence_processing_pipeline/tests/data/good-sample-sheet.csv"

minimap_database_paths = "/minimap/database/paths"
kraken2_database_path = "/kraken2/database/path"
queue_name = "queue_name"
node_count = 1
nprocs = 16
wall_time_limit = 8
jmem = "36k"


# Prefix for PBS -N e.g.: PBS -N myjobid_QCJob_NYU_BMS_Melanoma_13059
qiita_job_id = "myjobid"
pool_size = 64
max_array_length = 128




qc_job = QCJob(fastq_root_dir, output_path, sample_sheet_path,
                 minimap_database_paths, kraken2_database_path, queue_name,
                 node_count, nprocs, wall_time_limit, jmem, fastp_path,
                 minimap2_path, samtools_path, modules_to_load, qiita_job_id,
                 pool_size, max_array_length)


for project_name in qc_job.script_paths:
    foo = qc_job.script_paths[project_name]
    print(foo)



