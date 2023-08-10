from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from .models import Book, CommonDetail

class CommonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonDetail
        fields = (
            "id",
            "description",
            "creator",
        )
        extra_kwargs = {
            "description": {
                "read_only": True,
            },
        }

class BookSerializer(WritableNestedModelSerializer):
    detail = CommonDetailSerializer()
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "page_size",
            "version",
            "detail",
        )
        extra_kwargs = {
            "version": {
                "read_only": True,
            },
        }

    def create(self, validated_data):
        validated_data["version"] = Book.objects.filter(title__icontains=validated_data.get("title")).count()
        # validated_data["detail"].setdefault("description", validated_data["title"])
        self.initial_data["detail"].setdefault("description", validated_data["title"])
        return super().create(validated_data)
