from django.db import models

class BuildProject(models.Model):
    name = models.CharField(max_length=255)
    client = models.CharField(max_length=255, blank=True, default="")
    location = models.CharField(max_length=255, blank=True, default="")
    budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    spent = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("planning", "Planning"), ("in_progress", "In Progress"), ("on_hold", "On Hold"), ("completed", "Completed")], default="planning")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    progress = models.IntegerField(default=0)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class BuildTask(models.Model):
    title = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255, blank=True, default="")
    assigned_to = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("pending", "Pending"), ("in_progress", "In Progress"), ("completed", "Completed"), ("delayed", "Delayed")], default="pending")
    priority = models.CharField(max_length=50, choices=[("low", "Low"), ("medium", "Medium"), ("high", "High")], default="low")
    due_date = models.DateField(null=True, blank=True)
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Material(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=[("cement", "Cement"), ("steel", "Steel"), ("brick", "Brick"), ("sand", "Sand"), ("wood", "Wood"), ("electrical", "Electrical"), ("plumbing", "Plumbing")], default="cement")
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=255, blank=True, default="")
    unit_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    supplier = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("in_stock", "In Stock"), ("ordered", "Ordered"), ("delivered", "Delivered")], default="in_stock")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
