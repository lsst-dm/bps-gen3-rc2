#if [ -z "$EUPSTAG" ]; then
#    export EUPSTAG=`/usr/bin/date -d "+3days" +w_%Y_%U`    
#fi
EUPSTAG=w_2021_22
lsstsw_root=/software/lsstsw/stack


echo ${EUPSTAG}
source /opt/rh/devtoolset-8/enable
source ${lsstsw_root}/loadLSST.bash
setup lsst_distrib -t ${EUPSTAG}
setup faro

export OMP_NUM_THREADS=1

auth_path=/home/madamow/.lsst

# Postgres
export LSST_DB_AUTH=$auth_path/db-auth-rc.yaml
#export DAF_BUTLER_CONFIG_PATH=`pwd`
export PGPASSFILE=$auth_path/.pgpass

# HTCondor API
export PYTHONPATH=$PYTHONPATH:/usr/lib64/python3.6/site-packages

# Pegasus API
export PATH=$PATH:/project/production/pegasus/current/bin
export PYTHONPATH=$PYTHONPATH:/project/production/pegasus/current/lib64/python2.7/site-packages
