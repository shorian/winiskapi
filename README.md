# Winiskapi
*Work in progress.*

Winiskapi is a personal relationship manager with event planning features, [inspired by Monica](https://github.com/monicahq/monica). Winiskapi will offer a convenient, flexible interface for storing information and memories about your contacts, and will allow you to leverage that data to plan memorable events.

## Planned features
 - Create and update contacts without leaving the dashboard.
 - View all updates and events associated with a contact on their profile page. View a feed of all changes on the dashboard.
 - Receive email reminders for birthdays, anniversaries, and other significant dates and events.
 - **Interoperability**
   - Export contacts as vCard for use in other applications
   - Export events in iCal format
   - API for custom integrations
   - CalDAV sync would be nice.
 - Populate event planning pages with data from attendees.
   - Example: include your guests' food and drink preferences when planning a dinner party.
 - Record relationships between contacts.
   - Winiskapi can use this information to suggest additional guests or warn about potential conflicts when planning events.

## Total rewrite planned
I've learned a lot since I last touched this project, and some of my aims have also changed. I now use [Obsidian](https://obsidian.md/) to manage nearly all the information in my life, which makes interoperability a higher priority to me. Some of the design choices in the current codebase look a bit silly to me now.

Probable changes:
- API-first architecture (GraphQL may suit the data better than REST)
- Either rewrite frontend as a SPA, or use mainly vanilla JS
- Might move away from Python and Flask - it's tough to get the security/correctness guarantees I'm looking for out of a language that was never designed for that.
