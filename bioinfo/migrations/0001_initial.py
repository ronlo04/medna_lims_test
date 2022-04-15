from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utility.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utility', '0001_initial'),
        ('wet_lab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QualityMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_label', models.CharField('Analysis Label', max_length=255, unique=True)),
                ('process_location', models.ForeignKey(default=utility.models.get_default_process_location, on_delete=django.db.models.deletion.RESTRICT, to='utility.processlocation')),
                ('analysis_datetime', models.DateTimeField(verbose_name='Analysis DateTime')),
                ('analyst_first_name', models.CharField(max_length=255, verbose_name='Analyst First Name')),
                ('analyst_last_name', models.CharField(max_length=255, verbose_name='Analyst Last Name')),
                ('fastq_file', models.ManyToManyField(related_name='fastq_files', to='wet_lab.fastqfile', verbose_name='FASTQ Files')),
                ('seq_quality_check', models.CharField(choices=[('none', 'None'), ('manual_edit', 'Manually Edited')], max_length=50, verbose_name='Quality Check')),
                ('chimera_check', models.TextField(blank=True, verbose_name='Chimera Check')),
                ('trim_length_forward', models.PositiveIntegerField(verbose_name='Trim Length Forward (bp)')),
                ('trim_length_reverse', models.PositiveIntegerField(verbose_name='Trim Length Reverse (bp)')),
                ('min_read_length', models.PositiveIntegerField(verbose_name='Min Read Length (bp)')),
                ('max_read_length', models.PositiveIntegerField(verbose_name='Max Read Length (bp)')),
                ('analysis_sop', models.ForeignKey(to='utility.standardoperatingprocedure', on_delete=django.db.models.deletion.RESTRICT, verbose_name='Analysis SOP')),
                ('analysis_script_repo_url', models.URLField(default='https://github.com/Maine-eDNA', max_length=255, verbose_name='Repository URL')),
                ('quality_slug', models.TextField(max_length=255, verbose_name='Quality Slug')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Quality Metadata',
                'verbose_name_plural': 'Quality Metadata',
            },
        ),
        migrations.CreateModel(
            name='DenoiseClusterMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denoise_cluster_method_name', models.CharField(max_length=255, verbose_name='Method Name')),
                ('denoise_cluster_method_software_package', models.CharField(max_length=255, verbose_name='Software Package Name')),
                ('denoise_cluster_method_env_url', models.URLField(max_length=255, verbose_name='Environment File URL')),
                ('denoise_cluster_method_slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'DenoiseCluster Method',
                'verbose_name_plural': 'DenoiseCluster Methods',
                'unique_together': {('denoise_cluster_method_name', 'denoise_cluster_method_software_package')},
            },
        ),
        migrations.CreateModel(
            name='DenoiseClusterMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_label', models.CharField('Analysis Label', max_length=255, unique=True)),
                ('process_location', models.ForeignKey(default=utility.models.get_default_process_location, on_delete=django.db.models.deletion.RESTRICT, to='utility.processlocation')),
                ('quality_metadata', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.qualitymetadata')),
                ('analysis_datetime', models.DateTimeField(verbose_name='Analysis DateTime')),
                ('analyst_first_name', models.CharField(max_length=255, verbose_name='Analyst First Name')),
                ('analyst_last_name', models.CharField(max_length=255, verbose_name='Analyst Last Name')),
                ('denoise_cluster_method', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.denoiseclustermethod')),
                ('analysis_sop', models.ForeignKey(to='utility.standardoperatingprocedure', on_delete=django.db.models.deletion.RESTRICT, verbose_name='Analysis SOP')),
                ('analysis_script_repo_url', models.URLField(default='https://github.com/Maine-eDNA', max_length=255, verbose_name='Repository URL')),
                ('denoise_cluster_slug', models.SlugField(max_length=255, verbose_name='Metadata Slug')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'DenoiseCluster Metadata',
                'verbose_name_plural': 'DenoiseCluster Metadata',
            },
        ),
        migrations.CreateModel(
            name='FeatureOutput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_id', models.TextField(verbose_name='Feature ID')),
                ('feature_sequence', models.TextField(verbose_name='Feature Sequence')),
                ('feature_slug', models.SlugField(max_length=255, verbose_name='Feature Slug')),
                ('denoise_cluster_metadata', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.denoiseclustermetadata')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Feature Output',
                'verbose_name_plural': 'Feature Outputs',
            },
        ),
        migrations.CreateModel(
            name='FeatureRead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_reads', models.PositiveIntegerField(verbose_name='Number Reads')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.featureoutput')),
                ('extraction', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, blank=True, null=True, to='wet_lab.extraction')),
                ('read_slug', models.SlugField(max_length=255, verbose_name='Read Slug')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Feature Read',
                'verbose_name_plural': 'Feature Reads',
            },
        ),
        migrations.CreateModel(
            name='TaxonDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxon_domain', models.CharField(max_length=255, unique=True, verbose_name='Domain')),
                ('taxon_domain_slug', models.SlugField(max_length=255, verbose_name='Domain Slug')),
                ('taxon_url', models.URLField(blank=True, max_length=255, verbose_name='Taxon URL')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Taxon Domain',
                'verbose_name_plural': 'Taxon Domains',
            },
        ),
        migrations.CreateModel(
            name='TaxonKingdom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxon_kingdom', models.CharField(max_length=255, unique=True, verbose_name='Kingdom')),
                ('taxon_kingdom_slug', models.SlugField(max_length=255, verbose_name='Kingdom Slug')),
                ('taxon_domain', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.taxondomain')),
                ('taxon_url', models.URLField(blank=True, max_length=255, verbose_name='Taxon URL')),
                ('taxon_domain_slug', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Taxon Kingdom',
                'verbose_name_plural': 'Taxon Kingdoms',
            },
        ),
        migrations.CreateModel(
            name='TaxonSupergroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxon_supergroup', models.CharField(max_length=255, unique=True, verbose_name='Supergroup')),
                ('taxon_supergroup_slug', models.SlugField(max_length=255, verbose_name='Supergroup Slug')),
                ('taxon_kingdom', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.taxonkingdom')),
                ('taxon_url', models.URLField(blank=True, max_length=255, verbose_name='Taxon URL')),
                ('taxon_kingdom_slug', models.CharField(max_length=255, verbose_name='Kingdom')),
                ('taxon_domain_slug', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Taxon Supergroup',
                'verbose_name_plural': 'Taxon Supergroups',
            },
        ),
        migrations.CreateModel(
            name='TaxonPhylumDivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxon_phylum_division', models.CharField(max_length=255, unique=True, verbose_name='Phylum/Division')),
                ('taxon_phylum_division_slug', models.SlugField(max_length=255, verbose_name='Phylum Slug')),
                ('taxon_supergroup', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.taxonsupergroup')),
                ('taxon_url', models.URLField(blank=True, max_length=255, verbose_name='Taxon URL')),
                ('taxon_supergroup_slug', models.CharField(max_length=255, verbose_name='Supergroup')),
                ('taxon_kingdom_slug', models.CharField(max_length=255, verbose_name='Kingdom')),
                ('taxon_domain_slug', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Taxon Phylum/Division',
                'verbose_name_plural': 'Taxon Phyla/Divisions',
            },
        ),
        migrations.CreateModel(
            name='TaxonClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxon_class', models.CharField(max_length=255, unique=True, verbose_name='Class')),
                ('taxon_class_slug', models.SlugField(max_length=255, verbose_name='Class Slug')),
                ('taxon_phylum_division', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.taxonphylumdivision')),
                ('taxon_url', models.URLField(blank=True, max_length=255, verbose_name='Taxon URL')),
                ('taxon_phylum_division_slug', models.CharField(max_length=255, verbose_name='Phylum/Division')),
                ('taxon_supergroup_slug', models.CharField(max_length=255, verbose_name='Supergroup')),
                ('taxon_kingdom_slug', models.CharField(max_length=255, verbose_name='Kingdom')),
                ('taxon_domain_slug', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Taxon Class',
                'verbose_name_plural': 'Taxon Classes',
            },
        ),
        migrations.CreateModel(
            name='TaxonOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxon_order', models.CharField(max_length=255, unique=True, verbose_name='Order')),
                ('taxon_order_slug', models.SlugField(max_length=255, verbose_name='Order Slug')),
                ('taxon_class', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.taxonclass')),
                ('taxon_url', models.URLField(blank=True, max_length=255, verbose_name='Taxon URL')),
                ('taxon_class_slug', models.CharField(max_length=255, verbose_name='Class')),
                ('taxon_phylum_division_slug', models.CharField(max_length=255, verbose_name='Phylum/Division')),
                ('taxon_supergroup_slug', models.CharField(max_length=255, verbose_name='Supergroup')),
                ('taxon_kingdom_slug', models.CharField(max_length=255, verbose_name='Kingdom')),
                ('taxon_domain_slug', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Taxon Order',
                'verbose_name_plural': 'Taxon Orders',
            },
        ),
        migrations.CreateModel(
            name='TaxonFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxon_family', models.CharField(max_length=255, unique=True, verbose_name='Family')),
                ('taxon_family_slug', models.SlugField(max_length=255, verbose_name='Family Slug')),
                ('taxon_order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.taxonorder')),
                ('taxon_url', models.URLField(blank=True, max_length=255, verbose_name='Taxon URL')),
                ('taxon_order_slug', models.CharField(max_length=255, verbose_name='Order')),
                ('taxon_class_slug', models.CharField(max_length=255, verbose_name='Class')),
                ('taxon_phylum_division_slug', models.CharField(max_length=255, verbose_name='Phylum/Division')),
                ('taxon_supergroup_slug', models.CharField(max_length=255, verbose_name='Supergroup')),
                ('taxon_kingdom_slug', models.CharField(max_length=255, verbose_name='Kingdom')),
                ('taxon_domain_slug', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Taxon Family',
                'verbose_name_plural': 'Taxon Families',
            },
        ),
        migrations.CreateModel(
            name='TaxonGenus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxon_genus', models.CharField(max_length=255, unique=True, verbose_name='Genus')),
                ('taxon_genus_slug', models.SlugField(max_length=255, verbose_name='Genus Slug')),
                ('taxon_family', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.taxonfamily')),
                ('taxon_url', models.URLField(blank=True, max_length=255, verbose_name='Taxon URL')),
                ('taxon_family_slug', models.CharField(max_length=255, verbose_name='Family')),
                ('taxon_order_slug', models.CharField(max_length=255, verbose_name='Order')),
                ('taxon_class_slug', models.CharField(max_length=255, verbose_name='Class')),
                ('taxon_phylum_division_slug', models.CharField(max_length=255, verbose_name='Phylum/Division')),
                ('taxon_supergroup_slug', models.CharField(max_length=255, verbose_name='Supergroup')),
                ('taxon_kingdom_slug', models.CharField(max_length=255, verbose_name='Kingdom')),
                ('taxon_domain_slug', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Taxon Genus',
                'verbose_name_plural': 'Taxon Genera',
            },
        ),

        migrations.CreateModel(
            name='TaxonSpecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxon_species', models.CharField(max_length=255, unique=True, verbose_name='Species')),
                ('taxon_species_slug', models.SlugField(max_length=255, verbose_name='Species Slug')),
                ('taxon_genus', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.taxongenus')),
                ('taxon_common_name', models.CharField(max_length=255, verbose_name='Common Name')),
                ('is_endemic', models.CharField(choices=[(None, '(Unknown)'), ('no', 'No'), ('yes', 'Yes')], default='yes', max_length=50, verbose_name='Endemic to New England')),
                ('taxon_url', models.URLField(blank=True, max_length=255, verbose_name='Taxon URL')),
                ('taxon_genus_slug', models.CharField(max_length=255, verbose_name='Genus')),
                ('taxon_family_slug', models.CharField(max_length=255, verbose_name='Family')),
                ('taxon_order_slug', models.CharField(max_length=255, verbose_name='Order')),
                ('taxon_class_slug', models.CharField(max_length=255, verbose_name='Class')),
                ('taxon_phylum_division_slug', models.CharField(max_length=255, verbose_name='Phylum/Division')),
                ('taxon_supergroup_slug', models.CharField(max_length=255, verbose_name='Supergroup')),
                ('taxon_kingdom_slug', models.CharField(max_length=255, verbose_name='Kingdom')),
                ('taxon_domain_slug', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Taxon Species',
                'verbose_name_plural': 'Taxon Species',
            },
        ),
        migrations.CreateModel(
            name='ReferenceDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refdb_name', models.CharField(max_length=255, verbose_name='Reference Database Name')),
                ('refdb_version', models.CharField(max_length=255, verbose_name='Reference Database Version')),
                ('refdb_slug', models.SlugField(max_length=255, verbose_name='Reference Database Slug')),
                ('refdb_datetime', models.DateTimeField(verbose_name='Reference Database DateTime')),
                ('redfb_coverage_score', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Coverage Score (Percentage)', null=True)),
                ('refdb_repo_url', models.URLField(default='https://github.com/Maine-eDNA', max_length=255, verbose_name='Reference Database URL')),
                ('refdb_notes', models.TextField(verbose_name='Reference Database Notes', blank=True)),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Reference Database',
                'verbose_name_plural': 'Reference Databases',
                'unique_together': {('refdb_name', 'refdb_version')},
            },
        ),
        migrations.CreateModel(
            name='AnnotationMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annotation_method_name', models.CharField(max_length=255, verbose_name='Method Name')),
                ('annotation_method_software_package', models.CharField(max_length=255, verbose_name='Software Package Name')),
                ('annotation_method_env_url', models.URLField(max_length=255, verbose_name='Environment File URL')),
                ('annotation_method_name_slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Annotation Method',
                'verbose_name_plural': 'Annotation Methods',
                'unique_together': {('annotation_method_name', 'annotation_method_software_package')},
            },
        ),
        migrations.CreateModel(
            name='AnnotationMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_label', models.CharField(verbose_name='Analysis Label', max_length=255, unique=True)),
                ('analysis_datetime', models.DateTimeField(verbose_name='Analysis DateTime')),
                ('annotation_slug', models.SlugField(max_length=255, verbose_name='Annotation Metadata Slug')),
                ('analyst_first_name', models.CharField(max_length=255, verbose_name='Analyst First Name')),
                ('analyst_last_name', models.CharField(max_length=255, verbose_name='Analyst Last Name')),
                ('analysis_sop', models.ForeignKey(to='utility.standardoperatingprocedure', on_delete=django.db.models.deletion.RESTRICT, verbose_name='Analysis SOP')),
                ('annotation_method', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.annotationmethod')),
                ('analysis_script_repo_url', models.URLField(default='https://github.com/Maine-eDNA', max_length=255, verbose_name='Repository URL')),
                ('denoise_cluster_metadata', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.denoiseclustermetadata')),
                ('process_location', models.ForeignKey(default=utility.models.get_default_process_location, on_delete=django.db.models.deletion.RESTRICT, to='utility.processlocation')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Annotation Metadata',
                'verbose_name_plural': 'Annotation Metadata',
            },
        ),
        migrations.CreateModel(
            name='TaxonomicAnnotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.featureoutput')),
                ('annotation_metadata', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.annotationmetadata')),
                ('reference_database', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo.referencedatabase')),
                ('confidence', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True, verbose_name='Confidence')),
                ('ta_taxon', models.CharField(blank=True, max_length=255, verbose_name='Taxon')),
                ('ta_domain', models.CharField(blank=True, max_length=255, verbose_name='Domain')),
                ('ta_kingdom', models.CharField(blank=True, max_length=255, verbose_name='Kingdom')),
                ('ta_supergroup', models.CharField(blank=True, max_length=255, verbose_name='Supergroup')),
                ('ta_phylum_division', models.CharField(blank=True, max_length=255, verbose_name='Phylum/Division')),
                ('ta_class', models.CharField(blank=True, max_length=255, verbose_name='Class')),
                ('ta_order', models.CharField(blank=True, max_length=255, verbose_name='Order')),
                ('ta_family', models.CharField(blank=True, max_length=255, verbose_name='Family')),
                ('ta_genus', models.CharField(blank=True, max_length=255, verbose_name='Genus')),
                ('ta_species', models.CharField(blank=True, max_length=255, verbose_name='Species')),
                ('ta_common_name', models.CharField(blank=True, max_length=255, verbose_name='Common Name')),
                ('manual_domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_domain', to='bioinfo.taxondomain')),
                ('manual_kingdom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_kingdom', to='bioinfo.taxonkingdom')),
                ('manual_supergroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_supergroup', to='bioinfo.taxonsupergroup')),
                ('manual_phylum_division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_phylum_division', to='bioinfo.taxonphylumdivision')),
                ('manual_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_class', to='bioinfo.taxonclass')),
                ('manual_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_order', to='bioinfo.taxonorder')),
                ('manual_family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_family', to='bioinfo.taxonfamily')),
                ('manual_genus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_genus', to='bioinfo.taxongenus')),
                ('manual_species', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_species', to='bioinfo.taxonspecies')),
                ('manual_notes', models.TextField(verbose_name='Manual Annotation Notes', blank=True)),
                ('annotation_slug', models.SlugField(verbose_name='Annotation Slug', max_length=255)),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
            ],
            options={
                'verbose_name': 'Taxonomic Annotation',
                'verbose_name_plural': 'Taxonomic Annotations',
            },
        ),
    ]
