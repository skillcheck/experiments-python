set(
    FILES
    Stats.cpp
    Stats.hpp
)

add_library(
    stats SHARED
    ${FILES}
)
target_include_directories(
    stats
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}
)
set_target_properties(
    stats
    PROPERTIES
        WINDOWS_EXPORT_ALL_SYMBOLS ON
)
