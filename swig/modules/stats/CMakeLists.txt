find_package( SWIG REQUIRED )
include( ${SWIG_USE_FILE} )

find_package( Python COMPONENTS Interpreter Development )
find_package( PythonLibs 3 )
include_directories( ${PYTHON_INCLUDE_PATH} )
include_directories( ${CMAKE_CURRENT_SOURCE_DIR} )
include_directories( ${PROJECT_SOURCE_DIR}/swig )

set( CMAKE_SWIG_FLAGS "-py3" )

set_source_files_properties(
    stats.i
    PROPERTIES
        CPLUSPLUS ON
        SWIG_FLAGS "-c++"
)

swig_add_library(
    stats
    TYPE SHARED
    LANGUAGE python
    SOURCES
        stats.i
        stats-test.py
)
swig_link_libraries(
    stats
    stats
    ${PYTHON_LIBRARIES}
)

# adapted from: https://stackoverflow.com/questions/14784134/make-install-with-cmake-swig-python
execute_process(
    COMMAND python -m site --user-site
    OUTPUT_VARIABLE PYTHON_SITE_PACKAGES OUTPUT_STRIP_TRAILING_WHITESPACE
)
message( VERBOSE "PYTHON_SITE_PACKAGES = ${PYTHON_SITE_PACKAGES}")

install(
    TARGETS stats
    DESTINATION ${PYTHON_SITE_PACKAGES}
)
install(
    TARGETS _stats
    DESTINATION ${PYTHON_SITE_PACKAGES}
)
install(
    FILES ${CMAKE_CURRENT_BINARY_DIR}/stats.py
    DESTINATION ${PYTHON_SITE_PACKAGES}
)
