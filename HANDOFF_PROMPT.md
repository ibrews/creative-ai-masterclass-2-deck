# Part 2 maintenance

Edit tools/author_part2.py for lesson text. Run it, then tools/build_student_workbook.py. Copy classroom/start-here.html to workshop/Start Here.html. Preserve native builder changes in workshop/Unreal/Content/Python/small_worlds.py. Never overwrite existing student maps. Keep November 12, 2026, 11a–1p ET as the class date. Branding: Alex Coulombe Presents. Validate actual Unreal outputs separately from HTML and source syntax.

The shipped native assets were built from an empty Starter in Windows 5.9.0 CL60351404 and reopened in a second editor process. See evidence JSON and README for scope. Re-export PDFs with tools/export_classroom.mjs before packaging; tools/package_workshop.py validates all archived hashes. Publish only to this talk’s own origin/main.
