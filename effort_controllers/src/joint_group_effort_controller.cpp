// Copyright 2020 PAL Robotics S.L.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <string>

#include "hardware_interface/types/hardware_interface_type_values.hpp"
#include "effort_controllers/joint_group_effort_controller.hpp"
#include "rclcpp/logging.hpp"
#include "rclcpp/parameter.hpp"

namespace effort_controllers
{
using CallbackReturn = JointGroupEffortController::CallbackReturn;

JointGroupEffortController::JointGroupEffortController()
: forward_command_controller::ForwardCommandController()
{
  logger_name_ = "joint effort controller";
  interface_name_ = hardware_interface::HW_IF_EFFORT;
}

controller_interface::return_type
JointGroupEffortController::init(
  const std::string & controller_name)
{
  auto ret = ForwardCommandController::init(controller_name);
  if (ret != controller_interface::return_type::SUCCESS) {
    return ret;
  }

  try {
    // undeclare interface parameter used in the general forward_command_controller
    get_node()->undeclare_parameter("interface_name");
  } catch (const std::exception & e) {
    fprintf(stderr, "Exception thrown during init stage with message: %s \n", e.what());
    return controller_interface::return_type::ERROR;
  }

  return controller_interface::return_type::SUCCESS;
}

CallbackReturn JointGroupEffortController::on_deactivate(
  const rclcpp_lifecycle::State & previous_state)
{
  auto ret = ForwardCommandController::on_deactivate(previous_state);

  // stop all joints
  for (auto & command_interface : command_interfaces_) {
    command_interface.set_value(0.0);
  }

  return ret;
}

}  // namespace effort_controllers

#include "pluginlib/class_list_macros.hpp"

PLUGINLIB_EXPORT_CLASS(
  effort_controllers::JointGroupEffortController, controller_interface::ControllerInterface)
