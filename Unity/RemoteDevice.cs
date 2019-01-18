using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.NetworkInformation;
using System.Net.Sockets;
using System.Text.RegularExpressions;
using Sirenix.OdinInspector;
using UnityEngine;
using UnityEngine.Networking;
using Newtonsoft.Json;
using dt = System.DateTime;

namespace Landline
{
	[System.Serializable]
	public struct RemoteDevice
	{
		[ReadOnly]
		public string name, address, timestamp;

		[ReadOnly]
		public int port;

		/// <summary>
		/// How long (in seconds) since this device was updated.
		/// </summary>
		[ShowInInspector]
		public double age => (dt.Now - dt.Parse( timestamp, null )).TotalSeconds;

		public override string ToString ()
		{
			return $"{name} @{address}:{port} ({timestamp})";
		}
	}
}
