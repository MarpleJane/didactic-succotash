#coding: utf-8


INSERT_CHAPTER = """
    INSERT INTO chapter_plot(chapter_name, position, plot_json, type_id, description)
        VALUES(%(plot_name)s, %(position)s, %(plot_json)s, %(type_id)s, %(description)s)
"""

CHAPTER_TYPE_SUM = """
    SELECT COALESCE(COUNT(*), 0) AS total FROM chapter_plot
        WHERE type_id = %(type_id)s AND delete = 0
"""

CHAPTER_LIMIT = """
   SELECT id, plot_name, position, plot_json::varchar, type_id, description FROM chapter_plot
       WHERE type_id = %(type_id)s AND delete = 0
       ORDER BY position
       LIMIT %(limit)s OFFSET %(offset)s
"""

FIND_CHAPTER = """
    SELECT * FROM chapter_plot
        WHERE id = %(plot_id)s
"""

UPDATE_CHAPTER = """
    UPDATE chapter_plot
        SET description=%(description)s, plot_name=%(plot_name)s, position=%(position)s, plot_json=%(plot_json)s, update_time=%(update_time)s
        WHERE id = %(plot_id)s
"""

# DELETE_CHAPTER = """
#     DELETE FROM chapter_plot
#         WHERE id = %(plot_id)s
# """
DELETE_CHAPTER = """
    UPDATE chapter_plot
        SET delete = 1, update_time = %(update_time)s
        WHERE id = %(plot_id)s
"""

INSERT_SIMULATION = """
    INSERT INTO simulation_plot(cover_path, plot_name, position, plot_json, type_id)
        VALUES(%(cover_path)s, %(plot_name)s, %(position)s, %(plot_json)s, %(type_id)s)
"""

SIMULATION_TYPE_SUM = """
    SELECT COALESCE(COUNT(*), 0) AS total FROM simulation_plot
        WHERE type_id = %(type_id)s AND delete = 0
"""

SIMULATION_LIMIT = """
   SELECT id, plot_name, cover_path, position, plot_json::varchar, type_id FROM simulation_plot
       WHERE type_id = %(type_id)s AND delete = 0
       ORDER BY position
       LIMIT %(limit)s OFFSET %(offset)s
"""

FIND_SIMULATION = """
    SELECT * FROM simulation_plot
        WHERE id = %(plot_id)s
"""

UPDATE_SIMULATION = """
    UPDATE simulation_plot
        SET cover_path=%(cover_path)s, plot_name=%(plot_name)s, position=%(position)s, plot_json=%(plot_json)s, update_time=%(update_time)s
        WHERE id = %(plot_id)s
"""

# DELETE_SIMULATION = """
#     DELETE FROM simulation_plot
#         WHERE id = %(plot_id)s
# """
DELETE_SIMULATION = """
    UPDATE simulation_plot
        SET delete = 1, update_time = %(update_time)s
        WHERE id = %(plot_id)s
"""

CHAPTER = {
    'INSERT_CHAPTER': INSERT_CHAPTER,
    'CHAPTER_TYPE_SUM': CHAPTER_TYPE_SUM,
    'CHAPTER_LIMIT': CHAPTER_LIMIT,
    'FIND_CHAPTER': FIND_CHAPTER,
    'UPDATE_CHAPTER': UPDATE_CHAPTER,
    'DELETE_CHAPTER': DELETE_CHAPTER,
    }

SIMULATION = {
    'INSERT_SIMULATION': INSERT_SIMULATION,
    'SIMULATION_TYPE_SUM': SIMULATION_TYPE_SUM,
    'SIMULATION_LIMIT': SIMULATION_LIMIT,
    'FIND_SIMULATION': FIND_SIMULATION,
    'UPDATE_SIMULATION': UPDATE_SIMULATION,
    'DELETE_SIMULATION': DELETE_SIMULATION,
    }
