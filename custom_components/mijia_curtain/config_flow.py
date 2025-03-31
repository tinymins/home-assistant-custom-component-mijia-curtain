"""Config flow for Mijia Curtain integration."""
from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME, CONF_HOST, CONF_TOKEN, CONF_MODEL, CONF_SCAN_INTERVAL
from homeassistant.core import callback

from .const import DOMAIN

class MijiaCurtainConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Mijia Curtain."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Check if device already configured
            await self.async_set_unique_id(user_input[CONF_HOST])
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_NAME): str,
                    vol.Required(CONF_HOST): str,
                    vol.Required(CONF_TOKEN): str,
                    vol.Optional(CONF_MODEL): str,
                    vol.Optional(CONF_SCAN_INTERVAL, default=30): int,
                }
            ),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get options flow."""
        return OptionsFlowHandler(config_entry)

class OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        options = self.config_entry.options
        data = self.config_entry.data

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        CONF_TOKEN,
                        default=options.get(CONF_TOKEN, data.get(CONF_TOKEN, "")),
                    ): str,
                    vol.Optional(
                        CONF_MODEL,
                        default=options.get(CONF_MODEL, data.get(CONF_MODEL, "")),
                    ): str,
                    vol.Optional(
                        CONF_SCAN_INTERVAL,
                        default=options.get(CONF_SCAN_INTERVAL, data.get(CONF_SCAN_INTERVAL, 30)),
                    ): int,
                }
            ),
        )
