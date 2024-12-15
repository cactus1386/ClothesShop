# Generated by Django 4.2.7 on 2024-12-13 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_alter_category_image_alter_images_image"),
        ("cart", "0002_alter_cartitem_cart"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart_item",
                to="cart.cart",
            ),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="cart_product",
                to="products.product",
            ),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]