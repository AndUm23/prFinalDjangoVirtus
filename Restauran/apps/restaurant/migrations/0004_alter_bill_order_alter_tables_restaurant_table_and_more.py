# Generated by Django 4.2.11 on 2024-05-28 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0003_alter_shift_restaurant_alter_shift_waiter_tip_waiter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bill",
            name="order",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.DO_NOTHING, to="restaurant.order"
            ),
        ),
        migrations.AlterField(
            model_name="tables_restaurant",
            name="table",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.DO_NOTHING, to="restaurant.table"
            ),
        ),
        migrations.AlterField(
            model_name="tip_waiter",
            name="bill",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.DO_NOTHING, to="restaurant.bill"
            ),
        ),
        migrations.AlterField(
            model_name="tip_waiter",
            name="paid",
            field=models.BooleanField(default=False),
        ),
    ]