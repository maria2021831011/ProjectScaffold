from ProjectScaffold.scaffold import create_project


def test_create_project(tmp_path):
    project_name = tmp_path / "MyTestProject"
    create_project(
        name=str(project_name),
        backend='flask',
        frontend='react',
        db='sqlite'
    )

    assert (project_name / "models").exists()
    assert (project_name / "views").exists()
    assert (project_name / "controllers").exists()
    assert (project_name / "backend").exists()
    assert (project_name / "frontend").exists()
    assert (project_name / "db/sqlite.sql").exists()
