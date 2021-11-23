#!/bin/bash

set -e

if [ "$ENTRYPOINT_DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DJANGO_DATABASE_HOST $DJANGO_DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
	# Run and apply database migrations
	#echo "${0}: Creating database migrations"
	#python manage.py makemigrations users
	#python manage.py makemigrations utility
	#python manage.py makemigrations field_sites
	#python manage.py makemigrations sample_labels
	#python manage.py makemigrations field_survey
	#python manage.py makemigrations wet_lab
	#python manage.py makemigrations freezer_inventory
	#python manage.py makemigrations bioinfo_denoising
	#python manage.py makemigrations bioinfo_taxon
	echo "${0}: Applying database migrations"
	python manage.py migrate users
	python manage.py migrate utility
	python manage.py migrate field_sites
	python manage.py migrate sample_labels
	python manage.py migrate field_survey
	python manage.py migrate wet_lab
	python manage.py migrate freezer_inventory
	python manage.py migrate bioinfo_denoising
	python manage.py migrate bioinfo_taxon
	python manage.py migrate
fi

if [ "x$DJANGO_SUPERUSER_CREATE" = 'xon' ]; then
	# Apply createsuperuser
	echo "${0}: Creating superuser"
	python manage.py createsuperuser --no-input
fi

if [ "x$DJANGO_DEFAULT_GROUPS_CREATE" = 'xon' ]; then
 	echo "${0}: Creating permissions groups"
 	python manage.py create_default_groups
fi

if [ "x$DJANGO_DEFAULT_USERS_CREATE" = 'xon' ]; then
 	echo "${0}: Creating default users"
 	python manage.py loaddata fixtures/prod/medna_metadata_agol_usernames.json
fi

if [ "x$DJANGO_DATABASE_FLUSH" = 'xon' ]; then
 	echo "${0}: Flushing database"
 	python manage.py flush --no-input
fi

if [ "x$DJANGO_DATABASE_LOADDATA" = 'xon' ]; then
	# Load fixtures
	echo "${0}: Loading fixtures"
	# utility
	python manage.py loaddata fixtures/prod/utility_grant.json
  python manage.py loaddata fixtures/prod/utility_project.json
  python manage.py loaddata fixtures/prod/utility_processlocation.json
  # field_sites
  python manage.py loaddata fixtures/prod/field_sites_envobiomefirst.json
  python manage.py loaddata fixtures/prod/field_sites_envobiomesecond.json
  python manage.py loaddata fixtures/prod/field_sites_envobiomethird.json
  python manage.py loaddata fixtures/prod/field_sites_envobiomefourth.json
  python manage.py loaddata fixtures/prod/field_sites_envobiomefifth.json
  python manage.py loaddata fixtures/prod/field_sites_envofeaturefirst.json
  python manage.py loaddata fixtures/prod/field_sites_envofeaturesecond.json
  python manage.py loaddata fixtures/prod/field_sites_envofeaturethird.json
  python manage.py loaddata fixtures/prod/field_sites_envofeaturefourth.json
  python manage.py loaddata fixtures/prod/field_sites_envofeaturefifth.json
  python manage.py loaddata fixtures/prod/field_sites_envofeaturesixth.json
  python manage.py loaddata fixtures/prod/field_sites_envofeatureseventh.json
  python manage.py loaddata fixtures/prod/field_sites_system.json
  python manage.py loaddata fixtures/prod/field_sites_watershed.json
  python manage.py loaddata fixtures/prod/field_sites_fieldsite.json
  # sample_labels
  python manage.py loaddata fixtures/prod/sample_labels_sampletype.json
  python manage.py loaddata fixtures/prod/sample_labels_samplematerial.json
  python manage.py loaddata fixtures/prod/sample_labels_samplelabelrequest.json
  python manage.py loaddata fixtures/prod/sample_labels_samplebarcode.json
  # field_survey_etl
  python manage.py loaddata fixtures/prod/field_survey_fieldsurveyetl.json
  python manage.py loaddata fixtures/prod/field_survey_fieldcrewetl.json
  python manage.py loaddata fixtures/prod/field_survey_envmeasurementetl.json
  python manage.py loaddata fixtures/prod/field_survey_fieldcollectionetl.json
  python manage.py loaddata fixtures/prod/field_survey_samplefilteretl.json
  # field_survey
  python manage.py loaddata fixtures/prod/field_survey_fieldsurvey.json
  python manage.py loaddata fixtures/prod/field_survey_fieldcrew.json
  python manage.py loaddata fixtures/prod/field_survey_envmeasurement.json
  python manage.py loaddata fixtures/prod/field_survey_fieldcollection.json
  python manage.py loaddata fixtures/prod/field_survey_watercollection.json
  python manage.py loaddata fixtures/prod/field_survey_sedimentcollection.json
  python manage.py loaddata fixtures/prod/field_survey_fieldsample.json
  python manage.py loaddata fixtures/prod/field_survey_filtersample.json
  python manage.py loaddata fixtures/prod/field_survey_subcoresample.json
  # wet_lab
  python manage.py loaddata fixtures/prod/wet_lab_primerpair.json
  python manage.py loaddata fixtures/prod/wet_lab_indexremovalmethod.json
  python manage.py loaddata fixtures/prod/wet_lab_sizeselectionmethod.json
  python manage.py loaddata fixtures/prod/wet_lab_quantificationmethod.json
  python manage.py loaddata fixtures/prod/wet_lab_extractionmethod.json
  python manage.py loaddata fixtures/prod/wet_lab_indexpair.json
  python manage.py loaddata fixtures/prod/wet_lab_extraction.json
  python manage.py loaddata fixtures/prod/wet_lab_libraryprep.json
  python manage.py loaddata fixtures/prod/wet_lab_pooledlibrary.json
  python manage.py loaddata fixtures/prod/wet_lab_finalpooledlibrary.json
  python manage.py loaddata fixtures/prod/wet_lab_runprep.json
  python manage.py loaddata fixtures/prod/wet_lab_runresult.json
  # freezer_inventory
  python manage.py loaddata fixtures/prod/freezer_inventory_freezer.json
  python manage.py loaddata fixtures/prod/freezer_inventory_freezerrack.json
  python manage.py loaddata fixtures/prod/freezer_inventory_freezerbox.json
  python manage.py loaddata fixtures/prod/freezer_inventory_freezerinventory.json
  python manage.py loaddata fixtures/prod/freezer_inventory_freezercheckout.json
  # bioinfo_denoising
  python manage.py loaddata fixtures/prod/bioinfo_denoising_denoisingmethod.json
  python manage.py loaddata fixtures/prod/bioinfo_denoising_denoisingmetadata.json
  python manage.py loaddata fixtures/prod/bioinfo_denoising_ampliconsequencevariant.json
  python manage.py loaddata fixtures/prod/bioinfo_denoising_asvread.json
  # bioinfo_taxon
  python manage.py loaddata fixtures/prod/bioinfo_taxon_referencedatabase.json
  python manage.py loaddata fixtures/prod/bioinfo_taxon_taxondomain.json
  python manage.py loaddata fixtures/prod/bioinfo_taxon_taxonkingdom.json
  python manage.py loaddata fixtures/prod/bioinfo_taxon_taxonphylum.json
  python manage.py loaddata fixtures/prod/bioinfo_taxon_taxonclass.json
  python manage.py loaddata fixtures/prod/bioinfo_taxon_taxonorder.json
  python manage.py loaddata fixtures/prod/bioinfo_taxon_taxonfamily.json
  python manage.py loaddata fixtures/prod/bioinfo_taxon_taxongenus.json
  python manage.py loaddata fixtures/prod/bioinfo_taxon_taxonspecies.json
  python manage.py loaddata fixtures/prod/bioinfo_taxon_annotationmethod.json
  python manage.py loaddata fixtures/prod/bioinfo_taxon_annotationmetadata.json
  python manage.py loaddata fixtures/prod/bioinfo_taxon_taxonomicannotation.json
fi

# Start server
echo "${0}: Starting server"
gunicorn --bind 0.0.0.0:8000 medna_metadata.wsgi \
--workers 3 --log-level=info \
--log-syslog || exit 1

exec "$@"