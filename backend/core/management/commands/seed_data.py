from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import BuildProject, BuildTask, Material
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusConstruction with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusconstruction.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if BuildProject.objects.count() == 0:
            for i in range(10):
                BuildProject.objects.create(
                    name=f"Sample BuildProject {i+1}",
                    client=f"Sample {i+1}",
                    location=f"Sample {i+1}",
                    budget=round(random.uniform(1000, 50000), 2),
                    spent=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["planning", "in_progress", "on_hold", "completed"]),
                    start_date=date.today() - timedelta(days=random.randint(0, 90)),
                    end_date=date.today() - timedelta(days=random.randint(0, 90)),
                    progress=random.randint(1, 100),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 BuildProject records created'))

        if BuildTask.objects.count() == 0:
            for i in range(10):
                BuildTask.objects.create(
                    title=f"Sample BuildTask {i+1}",
                    project_name=f"Sample BuildTask {i+1}",
                    assigned_to=f"Sample {i+1}",
                    status=random.choice(["pending", "in_progress", "completed", "delayed"]),
                    priority=random.choice(["low", "medium", "high"]),
                    due_date=date.today() - timedelta(days=random.randint(0, 90)),
                    cost=round(random.uniform(1000, 50000), 2),
                    notes=f"Sample notes for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 BuildTask records created'))

        if Material.objects.count() == 0:
            for i in range(10):
                Material.objects.create(
                    name=f"Sample Material {i+1}",
                    category=random.choice(["cement", "steel", "brick", "sand", "wood", "electrical", "plumbing"]),
                    quantity=random.randint(1, 100),
                    unit=f"Sample {i+1}",
                    unit_cost=round(random.uniform(1000, 50000), 2),
                    supplier=["TechVision Pvt Ltd","Global Solutions","Pinnacle Systems","Nova Enterprises","CloudNine Solutions","MetaForge Inc","DataPulse Analytics","QuantumLeap Tech","SkyBridge Corp","Zenith Innovations"][i],
                    status=random.choice(["in_stock", "ordered", "delivered"]),
                )
            self.stdout.write(self.style.SUCCESS('10 Material records created'))
