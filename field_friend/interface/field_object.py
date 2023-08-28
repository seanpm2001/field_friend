import numpy as np
from nicegui.elements.scene_objects import Curve, Extrusion, Group
from rosys.geometry import Spline

from ..navigation import FieldProvider


class field_object(Group):

    def __init__(self, field_provider: FieldProvider) -> None:
        super().__init__()

        self.field_provider = field_provider
        self.update()
        self.field_provider.FIELDS_CHANGED.register_ui(self.update)

    def update(self) -> None:
        [obj.delete() for obj in list(self.scene.objects.values()) if obj.name and obj.name.startswith('field_')]
        [obj.delete() for obj in list(self.scene.objects.values()) if obj.name and obj.name.startswith('obstacle_')]
        [obj.delete() for obj in list(self.scene.objects.values()) if obj.name and obj.name.startswith('row_')]
        with self.scene:
            for field in self.field_provider.fields:
                if len(field.outline) == 1:
                    outline = [[field.outline[0].x + 0.05 * np.cos(phi), field.outline[0].y + 0.05 * np.sin(phi)]
                               for phi in np.linspace(0, 2 * np.pi, 16, endpoint=False)]
                else:
                    outline = [[point.x, point.y] for point in field.outline]
                with self.scene:
                    Extrusion(outline, 0.5, wireframe=True).with_name(f'field_{field.id}').material('#63462D')

                for obstacle in field.obstacles:
                    outline = [[point.x, point.y] for point in obstacle.points]
                    Extrusion(outline, 0.1).with_name(f'obstacle_{obstacle.id}').material('#B80F0A')

                for row in field.rows:
                    if len(row.points) == 1:
                        outline = [[row.points[0].x + 0.05 * np.cos(phi), row.points[0].y + 0.05 * np.sin(phi)]
                                   for phi in np.linspace(0, 2 * np.pi, 16, endpoint=False)]
                    else:
                        for i in range(len(row.points) - 1):
                            spline = Spline.from_points(row.points[i], row.points[i + 1])
                            Curve(
                                [spline.start.x, spline.start.y, 0],
                                [spline.control1.x, spline.control1.y, 0],
                                [spline.control2.x, spline.control2.y, 0],
                                [spline.end.x, spline.end.y, 0],
                            ).material('green').with_name(f'row_{row.id}_{i}')
