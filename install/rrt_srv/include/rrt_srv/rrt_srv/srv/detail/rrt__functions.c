// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from rrt_srv:srv/Rrt.idl
// generated code does not contain a copyright notice
#include "rrt_srv/srv/detail/rrt__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `start`
// Member `goal`
#include "geometry_msgs/msg/detail/pose_stamped__functions.h"
// Member `map`
#include "nav_msgs/msg/detail/occupancy_grid__functions.h"

bool
rrt_srv__srv__Rrt_Request__init(rrt_srv__srv__Rrt_Request * msg)
{
  if (!msg) {
    return false;
  }
  // start
  if (!geometry_msgs__msg__PoseStamped__init(&msg->start)) {
    rrt_srv__srv__Rrt_Request__fini(msg);
    return false;
  }
  // goal
  if (!geometry_msgs__msg__PoseStamped__init(&msg->goal)) {
    rrt_srv__srv__Rrt_Request__fini(msg);
    return false;
  }
  // map
  if (!nav_msgs__msg__OccupancyGrid__init(&msg->map)) {
    rrt_srv__srv__Rrt_Request__fini(msg);
    return false;
  }
  return true;
}

void
rrt_srv__srv__Rrt_Request__fini(rrt_srv__srv__Rrt_Request * msg)
{
  if (!msg) {
    return;
  }
  // start
  geometry_msgs__msg__PoseStamped__fini(&msg->start);
  // goal
  geometry_msgs__msg__PoseStamped__fini(&msg->goal);
  // map
  nav_msgs__msg__OccupancyGrid__fini(&msg->map);
}

bool
rrt_srv__srv__Rrt_Request__are_equal(const rrt_srv__srv__Rrt_Request * lhs, const rrt_srv__srv__Rrt_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // start
  if (!geometry_msgs__msg__PoseStamped__are_equal(
      &(lhs->start), &(rhs->start)))
  {
    return false;
  }
  // goal
  if (!geometry_msgs__msg__PoseStamped__are_equal(
      &(lhs->goal), &(rhs->goal)))
  {
    return false;
  }
  // map
  if (!nav_msgs__msg__OccupancyGrid__are_equal(
      &(lhs->map), &(rhs->map)))
  {
    return false;
  }
  return true;
}

bool
rrt_srv__srv__Rrt_Request__copy(
  const rrt_srv__srv__Rrt_Request * input,
  rrt_srv__srv__Rrt_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // start
  if (!geometry_msgs__msg__PoseStamped__copy(
      &(input->start), &(output->start)))
  {
    return false;
  }
  // goal
  if (!geometry_msgs__msg__PoseStamped__copy(
      &(input->goal), &(output->goal)))
  {
    return false;
  }
  // map
  if (!nav_msgs__msg__OccupancyGrid__copy(
      &(input->map), &(output->map)))
  {
    return false;
  }
  return true;
}

rrt_srv__srv__Rrt_Request *
rrt_srv__srv__Rrt_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rrt_srv__srv__Rrt_Request * msg = (rrt_srv__srv__Rrt_Request *)allocator.allocate(sizeof(rrt_srv__srv__Rrt_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rrt_srv__srv__Rrt_Request));
  bool success = rrt_srv__srv__Rrt_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
rrt_srv__srv__Rrt_Request__destroy(rrt_srv__srv__Rrt_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    rrt_srv__srv__Rrt_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
rrt_srv__srv__Rrt_Request__Sequence__init(rrt_srv__srv__Rrt_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rrt_srv__srv__Rrt_Request * data = NULL;

  if (size) {
    data = (rrt_srv__srv__Rrt_Request *)allocator.zero_allocate(size, sizeof(rrt_srv__srv__Rrt_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rrt_srv__srv__Rrt_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rrt_srv__srv__Rrt_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
rrt_srv__srv__Rrt_Request__Sequence__fini(rrt_srv__srv__Rrt_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rrt_srv__srv__Rrt_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

rrt_srv__srv__Rrt_Request__Sequence *
rrt_srv__srv__Rrt_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rrt_srv__srv__Rrt_Request__Sequence * array = (rrt_srv__srv__Rrt_Request__Sequence *)allocator.allocate(sizeof(rrt_srv__srv__Rrt_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = rrt_srv__srv__Rrt_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
rrt_srv__srv__Rrt_Request__Sequence__destroy(rrt_srv__srv__Rrt_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    rrt_srv__srv__Rrt_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
rrt_srv__srv__Rrt_Request__Sequence__are_equal(const rrt_srv__srv__Rrt_Request__Sequence * lhs, const rrt_srv__srv__Rrt_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!rrt_srv__srv__Rrt_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
rrt_srv__srv__Rrt_Request__Sequence__copy(
  const rrt_srv__srv__Rrt_Request__Sequence * input,
  rrt_srv__srv__Rrt_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(rrt_srv__srv__Rrt_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    rrt_srv__srv__Rrt_Request * data =
      (rrt_srv__srv__Rrt_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!rrt_srv__srv__Rrt_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          rrt_srv__srv__Rrt_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!rrt_srv__srv__Rrt_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `path`
#include "nav_msgs/msg/detail/path__functions.h"

bool
rrt_srv__srv__Rrt_Response__init(rrt_srv__srv__Rrt_Response * msg)
{
  if (!msg) {
    return false;
  }
  // path
  if (!nav_msgs__msg__Path__init(&msg->path)) {
    rrt_srv__srv__Rrt_Response__fini(msg);
    return false;
  }
  return true;
}

void
rrt_srv__srv__Rrt_Response__fini(rrt_srv__srv__Rrt_Response * msg)
{
  if (!msg) {
    return;
  }
  // path
  nav_msgs__msg__Path__fini(&msg->path);
}

bool
rrt_srv__srv__Rrt_Response__are_equal(const rrt_srv__srv__Rrt_Response * lhs, const rrt_srv__srv__Rrt_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // path
  if (!nav_msgs__msg__Path__are_equal(
      &(lhs->path), &(rhs->path)))
  {
    return false;
  }
  return true;
}

bool
rrt_srv__srv__Rrt_Response__copy(
  const rrt_srv__srv__Rrt_Response * input,
  rrt_srv__srv__Rrt_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // path
  if (!nav_msgs__msg__Path__copy(
      &(input->path), &(output->path)))
  {
    return false;
  }
  return true;
}

rrt_srv__srv__Rrt_Response *
rrt_srv__srv__Rrt_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rrt_srv__srv__Rrt_Response * msg = (rrt_srv__srv__Rrt_Response *)allocator.allocate(sizeof(rrt_srv__srv__Rrt_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rrt_srv__srv__Rrt_Response));
  bool success = rrt_srv__srv__Rrt_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
rrt_srv__srv__Rrt_Response__destroy(rrt_srv__srv__Rrt_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    rrt_srv__srv__Rrt_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
rrt_srv__srv__Rrt_Response__Sequence__init(rrt_srv__srv__Rrt_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rrt_srv__srv__Rrt_Response * data = NULL;

  if (size) {
    data = (rrt_srv__srv__Rrt_Response *)allocator.zero_allocate(size, sizeof(rrt_srv__srv__Rrt_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rrt_srv__srv__Rrt_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rrt_srv__srv__Rrt_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
rrt_srv__srv__Rrt_Response__Sequence__fini(rrt_srv__srv__Rrt_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rrt_srv__srv__Rrt_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

rrt_srv__srv__Rrt_Response__Sequence *
rrt_srv__srv__Rrt_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  rrt_srv__srv__Rrt_Response__Sequence * array = (rrt_srv__srv__Rrt_Response__Sequence *)allocator.allocate(sizeof(rrt_srv__srv__Rrt_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = rrt_srv__srv__Rrt_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
rrt_srv__srv__Rrt_Response__Sequence__destroy(rrt_srv__srv__Rrt_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    rrt_srv__srv__Rrt_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
rrt_srv__srv__Rrt_Response__Sequence__are_equal(const rrt_srv__srv__Rrt_Response__Sequence * lhs, const rrt_srv__srv__Rrt_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!rrt_srv__srv__Rrt_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
rrt_srv__srv__Rrt_Response__Sequence__copy(
  const rrt_srv__srv__Rrt_Response__Sequence * input,
  rrt_srv__srv__Rrt_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(rrt_srv__srv__Rrt_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    rrt_srv__srv__Rrt_Response * data =
      (rrt_srv__srv__Rrt_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!rrt_srv__srv__Rrt_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          rrt_srv__srv__Rrt_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!rrt_srv__srv__Rrt_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
