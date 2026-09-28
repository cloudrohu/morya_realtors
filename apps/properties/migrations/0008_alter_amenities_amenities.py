import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_amenities'),
        ('properties_utility', '0001_initial'),  # Make sure this app/model exists
    ]

    operations = [
        # Drop the old foreign key column (bigint)
        migrations.RemoveField(
            model_name='amenities',
            name='amenities',
        ),
        # Add the new foreign key column (UUID)
        migrations.AddField(
            model_name='amenities',
            name='amenities',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='amenities',
                to='properties_utility.amenity',
            ),
        ),
    ]