# Generated by Django 3.2.5 on 2021-10-19 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utility.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utility', '0001_initial'),
        ('bioinfo_denoising', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('analysis_datetime', models.DateTimeField(verbose_name='Analysis DateTime')),
                ('annotation_slug', models.SlugField(max_length=255, verbose_name='Annotation Metadata Slug')),
                ('analyst_first_name', models.CharField(max_length=255, verbose_name='Analyst First Name')),
                ('analyst_last_name', models.CharField(max_length=255, verbose_name='Analyst Last Name')),
                ('analysis_sop_url', models.URLField(max_length=255, verbose_name='Analysis SOP URL')),
                ('analysis_script_repo_url', models.URLField(default='https://github.com/Maine-eDNA', max_length=255, verbose_name='Repository URL')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Annotation Metadata',
                'verbose_name_plural': 'Annotation Metadata',
            },
        ),
        migrations.CreateModel(
            name='ReferenceDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('refdb_name', models.CharField(max_length=255, verbose_name='Reference Database Name')),
                ('refdb_version', models.CharField(max_length=255, verbose_name='Reference Database Version')),
                ('refdb_slug', models.SlugField(max_length=255, verbose_name='Reference Database Slug')),
                ('refdb_datetime', models.DateTimeField(verbose_name='Reference Database DateTime')),
                ('redfb_coverage_score', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Coverage Score (Percentage)')),
                ('refdb_repo_url', models.URLField(default='https://github.com/Maine-eDNA', max_length=255, verbose_name='Reference Database URL')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reference Database',
                'verbose_name_plural': 'Reference Databases',
                'unique_together': {('refdb_name', 'refdb_version')},
            },
        ),
        migrations.CreateModel(
            name='TaxonClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('taxon_class_slug', models.SlugField(max_length=255, verbose_name='Class Slug')),
                ('taxon_class', models.CharField(max_length=255, unique=True, verbose_name='Class')),
                ('taxon_phylum', models.CharField(max_length=255, verbose_name='Phylum')),
                ('taxon_kingdom', models.CharField(max_length=255, verbose_name='Kingdom')),
                ('taxon_domain', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Taxon Class',
                'verbose_name_plural': 'Taxon Classes',
            },
        ),
        migrations.CreateModel(
            name='TaxonDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('taxon_domain_slug', models.SlugField(max_length=255, verbose_name='Domain Slug')),
                ('taxon_domain', models.CharField(max_length=255, unique=True, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Taxon Domain',
                'verbose_name_plural': 'Taxon Domains',
            },
        ),
        migrations.CreateModel(
            name='TaxonFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('taxon_family_slug', models.SlugField(max_length=255, verbose_name='Family Slug')),
                ('taxon_family', models.CharField(max_length=255, unique=True, verbose_name='Family')),
                ('taxon_order', models.CharField(max_length=255, verbose_name='Order')),
                ('taxon_class', models.CharField(max_length=255, verbose_name='Class')),
                ('taxon_phylum', models.CharField(max_length=255, verbose_name='Phylum')),
                ('taxon_kingdom', models.CharField(max_length=255, verbose_name='Kingdom')),
                ('taxon_domain', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
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
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('taxon_genus_slug', models.SlugField(max_length=255, verbose_name='Genus Slug')),
                ('taxon_genus', models.CharField(max_length=255, unique=True, verbose_name='Genus')),
                ('taxon_family', models.CharField(max_length=255, verbose_name='Order')),
                ('taxon_order', models.CharField(max_length=255, verbose_name='Order')),
                ('taxon_class', models.CharField(max_length=255, verbose_name='Class')),
                ('taxon_phylum', models.CharField(max_length=255, verbose_name='Phylum')),
                ('taxon_kingdom', models.CharField(max_length=255, verbose_name='Kingdom')),
                ('taxon_domain', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('taxon_family_slug', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo_taxon.taxonfamily')),
            ],
            options={
                'verbose_name': 'Taxon Genus',
                'verbose_name_plural': 'Taxon Genera',
            },
        ),
        migrations.CreateModel(
            name='TaxonKingdom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('taxon_kingdom_slug', models.SlugField(max_length=255, verbose_name='Kingdom Slug')),
                ('taxon_kingdom', models.CharField(max_length=255, unique=True, verbose_name='Kingdom')),
                ('taxon_domain', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('taxon_domain_slug', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo_taxon.taxondomain')),
            ],
            options={
                'verbose_name': 'Taxon Kingdom',
                'verbose_name_plural': 'Taxon Kingdoms',
            },
        ),
        migrations.CreateModel(
            name='TaxonSpecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('taxon_species_slug', models.SlugField(max_length=255, verbose_name='Species Slug')),
                ('taxon_species', models.CharField(max_length=255, unique=True, verbose_name='Species')),
                ('taxon_common_name', models.CharField(max_length=255, verbose_name='Common Name')),
                ('is_endemic', models.CharField(choices=[(None, '(Unknown)'), ('no', 'No'), ('yes', 'Yes')], default='yes', max_length=50, verbose_name='Endemic to New England')),
                ('taxon_genus', models.CharField(max_length=255, verbose_name='Genus')),
                ('taxon_family', models.CharField(max_length=255, verbose_name='Order')),
                ('taxon_order', models.CharField(max_length=255, verbose_name='Order')),
                ('taxon_class', models.CharField(max_length=255, verbose_name='Class')),
                ('taxon_phylum', models.CharField(max_length=255, verbose_name='Phylum')),
                ('taxon_kingdom', models.CharField(max_length=255, verbose_name='Kingdom')),
                ('taxon_domain', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('taxon_genus_slug', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo_taxon.taxongenus')),
            ],
            options={
                'verbose_name': 'Taxon Species',
                'verbose_name_plural': 'Taxon Species',
            },
        ),
        migrations.CreateModel(
            name='TaxonPhylum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('taxon_phylum_slug', models.SlugField(max_length=255, verbose_name='Phylum Slug')),
                ('taxon_phylum', models.CharField(max_length=255, unique=True, verbose_name='Phylum')),
                ('taxon_kingdom', models.CharField(max_length=255, verbose_name='Kingdom')),
                ('taxon_domain', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('taxon_kingdom_slug', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo_taxon.taxonkingdom')),
            ],
            options={
                'verbose_name': 'Taxon Phylum',
                'verbose_name_plural': 'Taxon Phyla',
            },
        ),
        migrations.CreateModel(
            name='TaxonOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('taxon_order_slug', models.SlugField(max_length=255, verbose_name='Order Slug')),
                ('taxon_order', models.CharField(max_length=255, unique=True, verbose_name='Order')),
                ('taxon_class', models.CharField(max_length=255, verbose_name='Class')),
                ('taxon_phylum', models.CharField(max_length=255, verbose_name='Phylum')),
                ('taxon_kingdom', models.CharField(max_length=255, verbose_name='Kingdom')),
                ('taxon_domain', models.CharField(max_length=255, verbose_name='Domain')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('taxon_class_slug', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo_taxon.taxonclass')),
            ],
            options={
                'verbose_name': 'Taxon Order',
                'verbose_name_plural': 'Taxon Orders',
            },
        ),
        migrations.CreateModel(
            name='TaxonomicAnnotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('confidence', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True, verbose_name='Confidence')),
                ('ta_taxon', models.CharField(blank=True, max_length=255, verbose_name='Taxon')),
                ('ta_domain', models.CharField(blank=True, max_length=255, verbose_name='Domain')),
                ('ta_kingdom', models.CharField(blank=True, max_length=255, verbose_name='Kingdom')),
                ('ta_phylum', models.CharField(blank=True, max_length=255, verbose_name='Phylum')),
                ('ta_class', models.CharField(blank=True, max_length=255, verbose_name='Class')),
                ('ta_order', models.CharField(blank=True, max_length=255, verbose_name='Order')),
                ('ta_family', models.CharField(blank=True, max_length=255, verbose_name='Family')),
                ('ta_genus', models.CharField(blank=True, max_length=255, verbose_name='Genus')),
                ('ta_species', models.CharField(blank=True, max_length=255, verbose_name='Species')),
                ('ta_common_name', models.CharField(blank=True, max_length=255, verbose_name='Common Name')),
                ('annotation_metadata', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo_taxon.annotationmetadata')),
                ('asv', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo_denoising.ampliconsequencevariant')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('manual_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_class', to='bioinfo_taxon.taxonclass')),
                ('manual_domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_domain', to='bioinfo_taxon.taxondomain')),
                ('manual_family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_family', to='bioinfo_taxon.taxonfamily')),
                ('manual_genus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_genus', to='bioinfo_taxon.taxongenus')),
                ('manual_kingdom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_kingdom', to='bioinfo_taxon.taxonkingdom')),
                ('manual_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_order', to='bioinfo_taxon.taxonorder')),
                ('manual_phylum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_phylum', to='bioinfo_taxon.taxonphylum')),
                ('manual_species', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manual_species', to='bioinfo_taxon.taxonspecies')),
                ('reference_database', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo_taxon.referencedatabase')),
            ],
            options={
                'verbose_name': 'Taxonomic Annotation',
                'verbose_name_plural': 'Taxonomic Annotations',
            },
        ),
        migrations.AddField(
            model_name='taxonfamily',
            name='taxon_order_slug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo_taxon.taxonorder'),
        ),
        migrations.AddField(
            model_name='taxonclass',
            name='taxon_phylum_slug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo_taxon.taxonphylum'),
        ),
        migrations.CreateModel(
            name='AnnotationMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Modified DateTime')),
                ('created_datetime', models.DateTimeField(auto_now=True, verbose_name='Created DateTime')),
                ('annotation_method_name', models.CharField(max_length=255, unique=True, verbose_name='Denoising Method Name')),
                ('annotation_method_name_slug', models.SlugField(max_length=255, verbose_name='Annotation Method Slug')),
                ('created_by', models.ForeignKey(default=utility.models.get_default_user, on_delete=models.SET(utility.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Annotation Method',
                'verbose_name_plural': 'Annotation Methods',
            },
        ),
        migrations.AddField(
            model_name='annotationmetadata',
            name='annotation_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo_taxon.annotationmethod'),
        ),
        migrations.AddField(
            model_name='annotationmetadata',
            name='denoising_metadata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bioinfo_denoising.denoisingmetadata'),
        ),
        migrations.AddField(
            model_name='annotationmetadata',
            name='process_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='utility.processlocation'),
        ),
    ]
